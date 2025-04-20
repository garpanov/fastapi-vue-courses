from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from auth.auth_reg import verify_jwt
from db.config import get_session
from for_profile.models_pydantic_logn import ModelCreateCourse
from for_profile.request_db import db_create_course, db_get_activated_course, db_add_activated_course, \
	db_confirm_lesson, db_get_information_about_lesson, db_get_information_course

router_profile = APIRouter()

async def check_jwt(request: Request):
	token = request.cookies.get('access_token')
	token = verify_jwt(token)

	return token

@router_profile.post('/create_course')
async def create_course(data: ModelCreateCourse, token = Depends(check_jwt), session: AsyncSession = Depends(get_session)):
	result = await db_create_course(data, session)
	return result

@router_profile.get('/to_activated_course/{id_course}')
async def add_to_activated_course(id_course: int, token = Depends(check_jwt), session: AsyncSession = Depends(get_session)):
	user_id = int(token['sub'])

	result = await db_add_activated_course(user_id, id_course, session)

	return result


@router_profile.get('/activated_course')
async def get_activated_course(token = Depends(check_jwt), session: AsyncSession = Depends(get_session)):
	user_id = int(token['sub'])

	all_courses = await db_get_activated_course(user_id, session)

	return all_courses

@router_profile.get('/confirm_lesson/{course_id}/{lesson_position}')
async def confirm_lesson(course_id: int, lesson_position: int, token = Depends(check_jwt), session: AsyncSession = Depends(get_session)):
	user_id = int(token['sub'])

	await db_confirm_lesson(user_id, course_id, lesson_position, session)

	return True

@router_profile.get('/info_course/{course_id}')
async def get_information_course(course_id: int, token = Depends(check_jwt), session: AsyncSession = Depends(get_session)):
	user_id = int(token['sub'])

	course = await db_get_information_course(user_id, course_id, session)

	return course

@router_profile.get('/about_lesson/{course_id}/{lesson_id}')
async def get_information_about_lesson(course_id: int, lesson_id: int, token = Depends(check_jwt), session: AsyncSession = Depends(get_session)):
	lesson = await db_get_information_about_lesson(course_id, lesson_id, session)

	return lesson
