from fastapi import APIRouter, Request, Depends

from db.config import get_session
from auth.auth_reg import verify_jwt
from for_admin.request_db import *
from for_admin.models_pydantic import ModelConfirmationAccept, ModelConfirmationCancel, ModelDeleteCourse

router_admin = APIRouter()

async def check_jwt_role(request: Request):
	token = request.cookies.get('access_token')
	decoded_token = verify_jwt(token)
	if decoded_token['role'] != 'admin':
		raise HTTPException(403, 'Forbidden')

	return decoded_token


@router_admin.get('/info_course/{id_course}')
async def get_info_course(id_course: int, decoded_token = Depends(check_jwt_role), session: AsyncSession = Depends(get_session)):
	full_course = await db_get_info_course(id_course, session)
	if not full_course:
		raise HTTPException(404, 'Item not found')

	return full_course

@router_admin.get('/all_confirmation')
async def all_confirmation(decoded_token = Depends(check_jwt_role), session: AsyncSession = Depends(get_session)):
	all_confirmation_courses = await db_get_confirmation(session)
	return all_confirmation_courses

@router_admin.get('/confirmation/{id_course}')
async def get_confirmation(id_course: int, decoded_token = Depends(check_jwt_role), session: AsyncSession = Depends(get_session)):
	full_course = await db_get_confirmation_detail(id_course, session)
	if not full_course:
		raise HTTPException(404, 'Item not found')

	return full_course

@router_admin.get('/confirmation/lesson/{id_course}/{id_lesson}')
async def get_confirmation_lesson(id_course: int, id_lesson: int, decoded_token = Depends(check_jwt_role), session: AsyncSession = Depends(get_session)):
	lesson = await db_get_confirmation_detail_lesson(id_course, id_lesson, session)

	return lesson

@router_admin.post('/confirmation_accept')
async def accept_confirmation(data: ModelConfirmationAccept, decoded_token = Depends(check_jwt_role),
                              session: AsyncSession = Depends(get_session)):

	result = await db_accept_confirmation(data, session)
	return result

@router_admin.post('/confirmation_cancel')
async def cancel_confirmation(data: ModelConfirmationCancel, decoded_token = Depends(check_jwt_role),
                              session: AsyncSession = Depends(get_session)):

	result = await db_cancel_confirmation(data, session)
	return result

@router_admin.delete('/delete_course')
async def delete_course(data: ModelDeleteCourse, decoded_token = Depends(check_jwt_role),
                        session: AsyncSession = Depends(get_session)):

	result = await db_delete_course(data, session)
	return result

