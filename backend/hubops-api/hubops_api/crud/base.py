from typing import Any, Generic, Type, TypeVar, Optional
from pydantic import BaseModel
from hubops_api import supabase

ModelType = TypeVar("ModelType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]) -> None:
        '''
        This is the base class for all CRUD operations.
        '''
        self.model = model

    def get(self, id:int) -> Optional[ModelType]:
        item = supabase.table(self.model.table_name).select('*').eq('id', id).execute()
        try:
            return item.data[0]
        except:
            return None
        
    def get_many(self) -> Optional[list[ModelType]]:
        items = supabase.table(self.model.table_name).select('*').execute()
        try:
            return items.data
        except:
            return None
        
    def create(self, obj_in: CreateSchemaType) -> ModelType:
        item = supabase.table(self.model.table_name).insert(obj_in.dict()).execute()
        try:
            return item.data
        except:
            return None
    
    def update(self, id: int, obj_in: UpdateSchemaType) -> ModelType:
        item = supabase.table(self.model.table_name).update(obj_in.dict()).eq('id', id).execute()
        try:
            return item.data
        except:
            return None
    
    def delete(self, id: int) -> None:
        item = supabase.table(self.model.table_name).delete().eq('id', id).execute()
        return