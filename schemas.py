from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    name: str 
    email: str
    password: str
    adm:  Optional[bool]

    class Configure:
        from_attributes = True

# class UserSchemaNoPassword(BaseModel):
#     name: str 
#     email: str
#     adm: Optional[bool]

#     class Configure:
#         from_attributes = True



class LoginSchema(BaseModel):
    email_login: str
    password_login: str

    class Configure:
        from_attributes = True


class LoginAthorizeSchema(BaseModel):
    name_login: str
    password_login: str

    class Configure:
        from_attributes = True



class TaskSchema(BaseModel):
    name_list: str
    tasks_list: list[str]

    class Configure:
        from_attributes = True


class SearchListSchema(BaseModel):
    name_list: str

    class Configure:
        from_attributes = True


class DeleteListSchema(BaseModel):
    name_list: str

    class Configure:
        from_attribute = True 


class PathListSchema(BaseModel):
    name_edited: str
    list_edited: list[str]

    class Configure:
        from_attribute = True
   