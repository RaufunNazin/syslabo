from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    user_id: Optional[int]
    first_name: str
    last_name: str
    primary_department_id: int
    primary_position: str
    start_date: int
    end_date: Optional[int] = None
    username: str
    email: EmailStr
    password: str
    role: int = 0 # 0 means user, 1 means admin

class Department(BaseModel):
    department_id: Optional[int]
    department_name: str
    parent_department_id: Optional[int] = None
    start_date: int
    end_date: Optional[int] = None

class UserPosition(BaseModel):
    id: Optional[int]
    user_id: int
    department_id: int
    position: str
    kenmu: bool
    start_date: int
    end_date: Optional[int] = None

class ChangeHistory(BaseModel):
    change_id: Optional[int]
    entity: str
    entity_id: int
    change_type: str
    changed_by: int
    change_date: int
    old_value: Optional[str]
    new_value: Optional[str]

class ResponseUser(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: int = 0 # 0 means user, 1 means admin
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    username: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int
    email: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: ResponseUser
    class Config:
        from_attributes = True
