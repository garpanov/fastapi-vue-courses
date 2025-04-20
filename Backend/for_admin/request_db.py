from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from db.models import ModelDBConfirmationCourses, ModelDBCourses, ModelDBCoursesLessons, ModelDBConfirmationCancel, \
	ModelDBConfirmationCoursesLessons
from for_admin.models_pydantic import ModelConfirmationAccept, ModelConfirmationCancel, ModelDeleteCourse


async def db_get_info_course(id_course, session: AsyncSession):
	full_course = (await session.execute(select(ModelDBCourses).where(ModelDBCourses.id == id_course)
	                                .options(selectinload(ModelDBCourses.lessons)))).scalar()

	response = {
		"id": full_course.id,
		"name": full_course.name,
		"short_description": full_course.short_description,
		"full_description": full_course.full_description,
		"image_main": full_course.image_main,
		"author": full_course.author_name,
		"lessons": [
			{
				"id": lesson.id,
				"name": lesson.name,
				"position": lesson.position,
				"url_video": lesson.url_video,
				"description": lesson.description,
			}
			for lesson in full_course.lessons
		]
	}
	return response

async def db_get_confirmation(session: AsyncSession):
	all_confirmation = (await session.execute(select(ModelDBConfirmationCourses))).scalars().all()
	return all_confirmation


async def db_get_confirmation_detail(id_course: int, session: AsyncSession):
	full_course = (await session.execute(select(ModelDBConfirmationCourses)
	                                          .where(ModelDBConfirmationCourses.id == id_course)
	                                          .options(selectinload(ModelDBConfirmationCourses.lessons)))).scalar()
	response = {
		"id": full_course.id,
		"name": full_course.name,
		"short_description": full_course.short_description,
		"full_description": full_course.full_description,
		"image_main": full_course.image_main,
		"author": full_course.author_name,
		"lessons": [
			{
				"id": lesson.id,
				"name": lesson.name,
				"position": lesson.position,
				"url_video": lesson.url_video,
				"description": lesson.description,
			}
			for lesson in full_course.lessons
		]
	}
	return response

async def db_get_confirmation_detail_lesson(id_course: int, id_lesson: int, session: AsyncSession):
	info_lesson = (await session.execute(select(ModelDBConfirmationCoursesLessons)
	                                     .where(ModelDBConfirmationCoursesLessons.id == id_lesson,
	                                            ModelDBConfirmationCoursesLessons.course_id_fk == id_course))).scalar()
	return info_lesson



async def db_accept_confirmation(data:ModelConfirmationAccept, session: AsyncSession):
	full_course = (await session.execute(select(ModelDBConfirmationCourses)
	                                          .where(ModelDBConfirmationCourses.id == data.id)
												.options(selectinload(ModelDBConfirmationCourses.lessons),
													selectinload(ModelDBConfirmationCourses.author)))).scalar()
	if not full_course:
		raise HTTPException(404, 'Item not found')

	new_lessons = [ModelDBCoursesLessons(position=lesson.position,
	                                     name=lesson.name,
	                                     description=lesson.description,
	                                     url_video=lesson.url_video) for lesson in full_course.lessons]

	new_course = ModelDBCourses(name=full_course.name, short_description=full_course.short_description,
	                            full_description=full_course.full_description, points=data.points,
	                            image_main=full_course.image_main, author=full_course.author, author_name=full_course.author.username,
	                            author_id_fk=full_course.author_id_fk, lessons=new_lessons)

	await session.delete(full_course)

	session.add(new_course)
	await session.commit()
	return True


async def db_cancel_confirmation(data:ModelConfirmationCancel, session: AsyncSession):
	full_course = (await session.execute(select(ModelDBConfirmationCourses)
	                                          .where(ModelDBConfirmationCourses.id == data.id)
												.options(selectinload(ModelDBConfirmationCourses.lessons),
													selectinload(ModelDBConfirmationCourses.author)))).scalar()
	if not full_course:
		raise HTTPException(404, 'Item not found')

	cause_cancel = ModelDBConfirmationCancel(name=full_course.name, author=full_course.author.username, cause=data.cause)
	await session.delete(full_course)
	session.add(cause_cancel)
	await session.commit()
	return True

async def db_delete_course(data: ModelDeleteCourse, session: AsyncSession):
	full_course = (await session.execute(select(ModelDBCourses)
	                                     .where(ModelDBCourses.id == data.id)
	                                     .options(selectinload(ModelDBCourses.lessons),
	                                              selectinload(ModelDBCourses.author)))).scalar()

	cause_delete = ModelDBConfirmationCancel(name=full_course.name, author=full_course.author.username,
	                                         cause=data.cause)

	await session.delete(full_course)
	session.add(cause_delete)
	await session.commit()
	return True
