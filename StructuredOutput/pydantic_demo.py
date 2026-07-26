from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name : str = 'John'
    age : Optional[int] = None # need to explicitely provide None for Optional
    email : EmailStr
    cgpa = float = Field(gt=0,lt=10.1,default=6,description='A decimal value representing the CGPA of the student.')

student_name = {'age' : '25', 'email' : 'abc@xyz.in', 'cgpa' : 9} # pydantic type coercion 25

student = Student(**student_name) # kwargs from dict, postional args from list/tuple

print(student)

student_dict = student.model_dump()
student_json = student.model_dump_json()