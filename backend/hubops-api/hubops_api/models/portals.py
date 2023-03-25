from pydantic import BaseModel, EmailStr
import uuid

class Portal(BaseModel):
    id: int
    portal_id: int
    refresh_token: str
    access_token: str
    expires_in: int
    portal_name: str
    installer_email: EmailStr

class PortalUser(BaseModel):
    id: int
    portal_id: int
    user_id: uuid.UUID