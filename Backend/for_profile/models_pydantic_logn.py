from pydantic import BaseModel

class ModelCreateLesson(BaseModel):
	position: int
	name: str
	description: str
	url_video: str


class ModelCreateCourse(BaseModel):
	name: str
	short_description: str
	full_description: str
	image_main: str
	author: str
	lessons: list[ModelCreateLesson]

