from pydantic import BaseModel

class ModelConfirmationAccept(BaseModel):
	id: int
	points: int

class ModelDeleteCourse(BaseModel):
	id: int
	cause: str

class ModelConfirmationCancel(ModelDeleteCourse):
	pass