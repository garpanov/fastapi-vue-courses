from fastapi import APIRouter, Response, Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta, datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
import os

from auth.models_pydantic import ModelAuthorization, ModelRegistration, ModelAuthentication
from auth.request_db import db_login_authorization, db_registration, db_login_authentication_request, \
	db_registration_authentication_request
from db.config import get_session

from dotenv import load_dotenv
load_dotenv()


auth2 = OAuth2PasswordBearer(tokenUrl='/token')

router_auth = APIRouter()

def create_jwt(data: dict, refresh_token: bool = False):
	expire = datetime.now(timezone.utc) + timedelta(minutes=15)
	if refresh_token:
		expire = datetime.now(timezone.utc) + timedelta(minutes=60)

	data.update({'exp': expire})
	token = jwt.encode(data, algorithm='HS256', key=os.getenv('SECRET_KEY'))
	return token

def verify_jwt(token: str, refresh_token: bool = False):
	type_token = 'Access'
	if refresh_token:
		type_token = 'Refresh'
	try:
		decoded = jwt.decode(token, key=os.getenv('SECRET_KEY'), algorithms=['HS256'])
		return decoded

	except ExpiredSignatureError:
		raise HTTPException(401, f'{type_token} token expired')

	except InvalidTokenError:
		raise HTTPException(401, f'Invalid {type_token} token')

@router_auth.post('/token')
async def token_login(data: ModelAuthorization, response: Response, session: AsyncSession = Depends(get_session)):
	account = await db_login_authorization(data, session)
	data_for_token = {'sub': str(account.id), 'role': 'user'}
	if account.role == 'admin':
		data_for_token['role'] = 'admin'

	access_token = create_jwt(data_for_token)
	refresh_token = create_jwt(data_for_token, refresh_token=True)

	response.set_cookie('access_token', access_token, httponly=True)
	response.set_cookie('refresh_token', refresh_token, httponly=True, path='/auth/refresh')
	return account.username

@router_auth.post('/registration')
async def token_registration(data: ModelRegistration, response: Response, session: AsyncSession = Depends(get_session)):
	account = await db_registration(data, session)
	data_for_token = {'sub': str(account.id), 'role': 'user'}
	if account.role == 'admin':
		data_for_token['role'] = 'admin'

	access_token = create_jwt(data_for_token)
	refresh_token = create_jwt(data_for_token, refresh_token=True)

	response.set_cookie('access_token', access_token, httponly=True)
	response.set_cookie('refresh_token', refresh_token, httponly=True, path='/auth/refresh')
	return data.username

@router_auth.post('/authentication_request')
async def info_token(data: ModelAuthentication, session: AsyncSession = Depends(get_session)):
	await db_login_authentication_request(data.email, session)
	return True

@router_auth.post('/authentication_request_registration')
async def info_token(data: ModelAuthentication, session: AsyncSession = Depends(get_session)):
	await db_registration_authentication_request(data.email, session)
	return True

@router_auth.get('/about_me')
async def info_token(request: Request):
	token = request.cookies.get('access_token')
	verify_jwt(token)
	return True

@router_auth.get('/about_me_admin')
async def info_admin_token(request: Request):
	token = request.cookies.get('access_token')
	decoded_token = verify_jwt(token)
	if decoded_token['role'] != 'admin':
		raise HTTPException(403, 'Forbidden')

	return True



@router_auth.get('/refresh')
async def refresh_access_token(request: Request, response: Response):
	refresh_token = request.cookies.get('refresh_token')
	result = verify_jwt(refresh_token, refresh_token=True)
	account_id = result['sub']
	role = 'user'
	if result['role'] == 'admin':
		role = 'admin'

	new_access_token = create_jwt({'sub': account_id, 'role': role})
	response.set_cookie('access_token', new_access_token, httponly=True)
	return True





