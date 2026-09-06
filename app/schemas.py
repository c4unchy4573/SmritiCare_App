# app/schemas.py
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
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

class SessionIn(BaseModel):
    gameId: str
    score: float
    accuracy: float = Field(ge=0.0, le=1.0)
    reactionTime: float | None = None
    mistakes: int = 0
    difficulty: int
    duration: int
    extra: dict = {}

class SessionOut(BaseModel):
    id: uuid.UUID
    patientId: uuid.UUID = Field(alias="patient_id")
    gameId: str = Field(alias="game_id")
    score: float
    accuracy: float
    reactionTime: float | None = Field(alias="reaction_time", default=None)
    mistakes: int
    difficulty: int
    duration: int
    createdAt: datetime = Field(alias="created_at")

    class Config:
        from_attributes = True
        populate_by_name = True

class PatientProfileOut(BaseModel):
    userId: uuid.UUID = Field(alias="user_id")
    fullName: str
    email: str
    languagePref: str = Field(alias="language_pref")
    baselineCompleted: bool = Field(alias="baseline_completed")

    class Config:
        from_attributes = True
        populate_by_name = True

class PatientProfileUpdate(BaseModel):
    languagePref: str | None = None
    baselineCompleted: bool | None = None

class CaregiverLinkIn(BaseModel):
    patientEmail: str