from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from db.models import ModelDBCourses

async def db_get_all_courses(session: AsyncSession):
	all_courses = (await session.execute(select(ModelDBCourses).limit(6))).scalars().all()

	response = [{'id': course.id,'name': course.name, 'short_description': course.short_description,
	             'points': course.points, 'image_main': course.image_main, 'author': course.author_name} for course in all_courses]

	return response

async def db_get_info_course(course_id:int, session: AsyncSession):
	info_course = (await session.execute(select(ModelDBCourses).where(ModelDBCourses.id == course_id)
	                                     .options(selectinload(ModelDBCourses.lessons))
	                                     .options(selectinload(ModelDBCourses.author)))).scalar()

	response = {
		"id": info_course.id,
		"name": info_course.name,
		"full_description": info_course.full_description,
		"author": info_course.author.username,
		"lessons": [
			{
				"position": lesson.position,
				'description': lesson.description,
				"name": lesson.name,
			}
			for lesson in info_course.lessons[:4]
		]
	}
	return response