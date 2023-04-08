from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional


class Package(BaseModel):
    id: int
    portal_id: int
    name: str
    status: str
    created_at: datetime
    created_short: date

    table_name: Optional[str] = 'packages'

class PackageError(BaseModel):
    id: int
    package_id: int
    error_message: str

    table_name: Optional[str] = 'package_errors'

class PackageDeployment(BaseModel):
    id: int
    created_at: datetime
    ended_at: datetime
    package_id: int
    status: str
    to_portal_id: int
    name: str

    table_name: Optional[str] = 'package_deployments'

class PackageComponent(BaseModel):
    id: int
    package_id: int
    property_id: int
    property_group_id: int
    component_type: str
    component_name: str

    table_name: Optional[str] = 'package_components'

class DeploymentLog(BaseModel):
    id: int
    created_at: datetime
    message: str
    deployment_id: int
    package_component_id: int
    is_error: bool

    table_name: Optional[str] = 'deployment_logs'