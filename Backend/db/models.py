from __future__ import annotations

from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship



class Base(DeclarativeBase):
	pass

connection_participate_lessons = Table(
	'connection_participate_lessons',
	Base.metadata,
	Column('id_lessons', ForeignKey('lessons.id'), primary_key=True),
	Column('id_participate', ForeignKey('course_participate.id'), primary_key=True)

)

class ModelDBUsers(Base):
	__tablename__ = 'users'
	id: Mapped[int] = mapped_column(primary_key=True)
	username: Mapped[str]
	email: Mapped[str]
	password: Mapped[str]
	role: Mapped[str]
	owner_courses: Mapped[list[ModelDBCourses]] = relationship(back_populates='author', uselist=True)
	confirmation_owner_courses: Mapped[list[ModelDBConfirmationCourses]] = relationship(back_populates='author')
	course_participate: Mapped[list[ModelDBCourseParticipate]] = relationship(back_populates='user', uselist=True)

class ModelDBCourses(Base):
	__tablename__ = 'courses'
	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str]
	short_description: Mapped[str]
	full_description: Mapped[str]
	points: Mapped[int]
	image_main: Mapped[str]
	author_name: Mapped[str]
	author: Mapped[ModelDBUsers] = relationship(back_populates='owner_courses')
	author_id_fk: Mapped[int] = mapped_column(ForeignKey('users.id'))
	list_participate: Mapped[list[ModelDBCourseParticipate]] = relationship(back_populates='course', uselist=True)
	lessons: Mapped[list[ModelDBCoursesLessons]] = relationship(back_populates='course', uselist=True, cascade='all, delete-orphan')

class ModelDBCoursesLessons(Base):
	__tablename__ = 'lessons'
	id: Mapped[int] = mapped_column(primary_key=True)
	position: Mapped[int]
	name: Mapped[str]
	description: Mapped[str]
	url_video: Mapped[str]
	course: Mapped[ModelDBCourses] = relationship(back_populates='lessons')
	course_id_fk: Mapped[int] = mapped_column(ForeignKey('courses.id'))
	completed_lessons: Mapped[list[ModelDBCourseParticipate]] = relationship(back_populates='completed_lessons',
	                                                                           secondary=connection_participate_lessons)

class ModelDBCourseParticipate(Base):
	__tablename__ = 'course_participate'
	id: Mapped[int] = mapped_column(primary_key=True)
	user_id_fk: Mapped[int] = mapped_column(ForeignKey('users.id'))
	user: Mapped[ModelDBUsers] = relationship(back_populates='course_participate')
	course: Mapped[ModelDBCourses] = relationship(back_populates='list_participate')
	course_id_fk: Mapped[int] = mapped_column(ForeignKey('courses.id'))
	completed_lessons: Mapped[list[ModelDBCoursesLessons]] = relationship(back_populates='completed_lessons',
	                                                                      secondary=connection_participate_lessons)

class ModelDBConfirmationCourses(Base):
	__tablename__ = 'confirmation_courses'
	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str]
	short_description: Mapped[str]
	full_description: Mapped[str]
	image_main: Mapped[str]
	author_name: Mapped[str]
	author: Mapped[ModelDBUsers] = relationship(back_populates='confirmation_owner_courses')
	author_id_fk: Mapped[int] = mapped_column(ForeignKey('users.id'))
	lessons: Mapped[list[ModelDBConfirmationCoursesLessons]] = relationship(back_populates='course', uselist=True,
	                                                                        cascade='all, delete-orphan')


class ModelDBConfirmationCoursesLessons(Base):
	__tablename__ = 'confirmation_courses_lessons'
	id: Mapped[int] = mapped_column(primary_key=True)
	position: Mapped[int]
	name: Mapped[str]
	description: Mapped[str]
	url_video: Mapped[str]
	course: Mapped[ModelDBConfirmationCourses | None] = relationship(back_populates='lessons')
	course_id_fk: Mapped[int] = mapped_column(ForeignKey('confirmation_courses.id'))

class ModelDBConfirmationCancel(Base):
	__tablename__ = 'confirmation_cancel'
	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str]
	author: Mapped[str]
	cause: Mapped[str]