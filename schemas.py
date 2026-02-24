from pydantic import BaseModel


class createStudent(BaseModel):
    student_name : str
    student_email: str
    student_password: str

class studentLogin(BaseModel):
    student_email:str
    student_password : str

class studentResponse(BaseModel):
    student_name:str
    student_email:str
    student_password : str


class token(BaseModel):
    access_token : str
    token_type: str