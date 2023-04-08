from pydantic import BaseModel
from typing import Optional

class Property(BaseModel):
    id: int
    portal_id: int
    internal_name: str
    label: str
    options: dict
    type: str
    field_type: str
    description: str
    form_field: bool
    hidden: bool
    display_order: int
    external_options: bool
    referenced_object_type: str
    calculation_formula: str
    modification_metadata: dict
    property_group: str
    object_type: str

    table_name: Optional[str] = 'properties'

class PropertyGroup(BaseModel):
    id: int
    internal_name: str
    label: str
    display_order: int
    object_type: str
    portal_id: int

    table_name: Optional[str] = 'property_groups'