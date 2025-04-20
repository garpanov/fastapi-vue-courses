from pydantic import BaseModel, EmailStr

class ModelBase(BaseModel):
	email: EmailStr
	password: str

class ModelRegistration(ModelBase):
	username:str
	pass

class ModelAuthentication(BaseModel):
	email: EmailStr

class ModelAuthorization(ModelBase):
	pass

