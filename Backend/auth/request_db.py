from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from auth.models_pydantic import ModelAuthentication, ModelAuthorization, ModelRegistration
from db.models import *
from auth.utils import *

async def db_login_authentication_request(email: str, session: AsyncSession):
	account = (await session.execute(select(ModelDBUsers).where(ModelDBUsers.email == email))).scalar_one_or_none()
	if not account:
		raise HTTPException(404, 'Not Found')

	return account

async def db_login_authentication(data: ModelAuthentication, session: AsyncSession):
	await db_login_authentication_request(data.email, session)
	return True

async def db_login_authorization(data: ModelAuthorization, session: AsyncSession):
	account = await db_login_authentication_request(data.email, session)
	verify = verify_password(data.password, account.password)
	if not verify:
		raise HTTPException(401, 'Unauthorized')

	return account

# ////////////////////////  REGISTRATION  ////////////////////////////

async def db_registration_authentication_request(email: str, session: AsyncSession, username: str | None = None):
	account = (await session.execute(select(ModelDBUsers).where(ModelDBUsers.email == email))).first()
	if account:
		raise HTTPException(409, 'Email already exists')

	if username:
		account = (await session.execute(select(ModelDBUsers).where(ModelDBUsers.username == username))).first()
		if account:
			raise HTTPException(409, 'Username already exists')

	return False

async def db_registration_authentication(data: ModelAuthentication, session: AsyncSession):
	await db_registration_authentication_request(data.email, session)

async def db_registration(data: ModelRegistration, session: AsyncSession):
	name = data.username[0].upper() + data.username[1:].lower()
	await db_registration_authentication_request(data.email, session, username=name)

	password = hash_password(data.password)
	account = ModelDBUsers(email=data.email, username=name, password=password, role='user')
	session.add(account)
	await session.commit()
	await session.refresh(account)

	return account


