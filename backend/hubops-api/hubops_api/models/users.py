from pydantic import BaseModel, EmailStr
import uuid

class User(BaseModel):
    id: uuid.UUID
    email: EmailStr
    encrypted_password: str