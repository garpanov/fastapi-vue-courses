from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from db.config import get_session
from main_menu.request_db import db_get_all_courses, db_get_info_course

router_main = APIRouter()

@router_main.get('/all_courses')
async def get_all_courses(session: AsyncSession = Depends(get_session)):
	all_courses = await db_get_all_courses(session)
	return all_courses

@router_main.get('/course/{course_id}')
async def get_info_course(course_id: int, session: AsyncSession = Depends(get_session)):
	info_course = await db_get_info_course(course_id, session)
	if not info_course:
		raise HTTPException(404, 'Course not found')


	return info_course