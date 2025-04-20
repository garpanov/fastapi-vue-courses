from urllib.parse import urlparse, parse_qs

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from for_profile.models_pydantic_logn import ModelCreateCourse
from db.models import ModelDBConfirmationCourses, ModelDBConfirmationCoursesLessons, ModelDBUsers, ModelDBCourses, \
	ModelDBCourseParticipate, ModelDBCoursesLessons

def get_youtube_embed_url(url: str) -> str:
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    video_id = query_params.get("v", [None])[0]

    return f"https://www.youtube.com/embed/{video_id}"


async def db_create_course(data: ModelCreateCourse, session: AsyncSession):
	author_name = data.author[0].upper() + data.author[1:].lower()
	author = (await session.execute(select(ModelDBUsers).where(ModelDBUsers.username == author_name))).scalar()
	lessons = [ModelDBConfirmationCoursesLessons(**lesson.model_dump(exclude={"url_video"}), url_video=get_youtube_embed_url(lesson.url_video)) for lesson in data.lessons]
	course = ModelDBConfirmationCourses(**data.model_dump(exclude={"lessons", "author"}), lessons=lessons, author=author, author_name=author_name)

	session.add(course)
	await session.commit()
	return True

async def db_get_information_course(user_id: int, course_id: int, session: AsyncSession):
	course = (await session.execute(select(ModelDBCourses).where(ModelDBCourses.id == course_id)
	                                .options(selectinload(ModelDBCourses.lessons)))).scalar()

	user = (await session.execute(select(ModelDBUsers).where(ModelDBUsers.id == user_id)
	                              .options(selectinload(ModelDBUsers.course_participate)
	                                       .selectinload(ModelDBCourseParticipate.completed_lessons)))).scalar()

	completed_lessons = user.course_participate[0].completed_lessons

	for lesson in course.lessons:
		if lesson in completed_lessons:
			lesson.completed = True
		else:
			lesson.completed = False

	return course

async def db_get_information_about_lesson(course_id: int, lesson_id: int, session: AsyncSession):
	lesson = (await session.execute(select(ModelDBCoursesLessons).where(ModelDBCoursesLessons.course_id_fk == course_id,
	                                                                    ModelDBCoursesLessons.id == lesson_id))).scalar()

	return lesson


async def db_add_activated_course(user_id: int, course_id: int, session: AsyncSession):
	course_activate = (await session.execute(select(ModelDBCourseParticipate).where(ModelDBCourseParticipate.user_id_fk == user_id,
	                                                                        ModelDBCourseParticipate.course_id_fk == course_id))).scalar()
	if course_activate:
		return False

	new_activated = ModelDBCourseParticipate(user_id_fk=user_id, course_id_fk=course_id)
	session.add(new_activated)
	await session.commit()

	return True


async def db_get_activated_course(user_id: int, session: AsyncSession):
	all_courses = (await session.execute(select(ModelDBUsers).where(ModelDBUsers.id == user_id)
	                                     .options(selectinload(ModelDBUsers.course_participate).selectinload(ModelDBCourseParticipate.course)))).scalar()

	courses = [course_part.course for course_part in all_courses.course_participate ]
	return courses

async def db_confirm_lesson(user_id: int, course_id: int, lesson_position: int, session: AsyncSession):
	get_lesson = (await session.execute(select(ModelDBCoursesLessons).where(ModelDBCoursesLessons.course_id_fk == course_id,
	                                                                        ModelDBCoursesLessons.position == lesson_position))).scalar()

	course_participate = (await session.execute(select(ModelDBCourseParticipate).where(ModelDBCourseParticipate.course_id_fk == course_id,
	                                                                                   ModelDBCourseParticipate.user_id_fk == user_id)
	                                            .options(selectinload(ModelDBCourseParticipate.completed_lessons)))).scalar()

	if get_lesson in course_participate.completed_lessons:
		return False

	course_participate.completed_lessons.append(get_lesson)
	session.add(course_participate)
	await session.commit()
	return True
