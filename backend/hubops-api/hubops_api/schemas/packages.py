from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional


# PACKAGE
class PackageBase(BaseModel):
    portal_id: int
    name: str


class PackageCreate(PackageBase):
    portal_id: int
    name: str

class PackageInDBBase(PackageBase):
    id: int
    status: str
    created_at: Optional[datetime]
    created_short: Optional[date]

class Package(PackageInDBBase):
    pass

# PACKAGE ERROR
class PackageError(BaseModel):
    id: int
    package_id: int
    error_message: str


# PACKAGE DEPLOYMENT
class PackageDeploymentBase(BaseModel):
    package_id: Optional[int]
    to_portal_id: Optional[int]
    name: Optional[str]

class PackageDeploymentCreate(PackageDeploymentBase):
    pass

class PackageDeploymentUpdate(PackageDeploymentBase):
    id: int
    status: str

class PackageDeploymentInDBBase(PackageDeploymentBase):
    id: int
    created_at: Optional[datetime]
    ended_at: Optional[datetime]
    status: str

class PackageDeployment(PackageDeploymentInDBBase):
    pass


# PACKAGE COMPONENT
class PackageComponentBase(BaseModel):
    package_id: int
    property_id: Optional[int]
    property_group_id: Optional[int]
    component_type: str
    component_name: str

class PackageComponentCreate(PackageComponentBase):
    pass

class PackageComponentInDBBase(PackageComponentBase):
    id: int

class PackageComponent(PackageComponentInDBBase):
    pass


# DEPLOYMENT LOG
class DeploymentLog(BaseModel):
    id: int
    created_at: Optional[datetime]
    message: str
    deployment_id: int
    package_component_id: int
    is_error: bool