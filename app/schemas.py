from pydantic import BaseModel, EmailStr
import uuid

class RegisterIn(BaseModel):
    email: EmailStr
    password: str
    role: str  # "patient" | "caregiver"
    full_name: str

class LoginIn(BaseModel):
    email: EmailStr
    password: str

class TokenOut(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class UserOut(BaseModel):
    id: uuid.UUID
    email: EmailStr
    role: str
    full_name: str

    class Config:
        from_attributes = True