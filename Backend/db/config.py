from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import asyncio
import os

from db.models import *
from dotenv import load_dotenv
load_dotenv()


engine = create_async_engine(os.getenv('POSTGRES_ASYNC'), echo=True)
Async_session = async_sessionmaker(bind=engine)

async def get_session():
	async with Async_session() as session:
		yield session

async def init_db():
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)

async def create_account():
	async with Async_session() as session:
		admin = ModelDBUsers(username='Garpanova',
		                     email='sashaprilep123654A@gmail.com',
		                     password='$2b$12$pV2DBl4DVuzV41QBx03fKum5iedJUtLqxuUxBvwNKHcoRi6UPVBn.',
		                     role='admin')

		user = ModelDBUsers(username='Garpanov',
		                     email='sashaprilep123654@gmail.com',
		                     password='$2b$12$pV2DBl4DVuzV41QBx03fKum5iedJUtLqxuUxBvwNKHcoRi6UPVBn.',
		                     role='user')

		session.add_all([admin, user])
		await session.commit()

async def main():
	await init_db()
	await create_account()

if __name__ == '__main__':

	asyncio.run(main())