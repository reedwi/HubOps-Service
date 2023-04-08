from hubops_api.crud.base import CRUDBase
from typing import Optional
from hubops_api import supabase
from hubops_api.models.packages import DeploymentLog
from hubops_api.schemas.packages import DeploymentLog as DeploymentLogSchema

class CRUDDeploymentLog(CRUDBase[DeploymentLogSchema]):
    def get_logs(self, deployment_id: int) -> Optional[list[DeploymentLogSchema]]:
        deployment_logs = supabase.table('deployment_logs').select().eq('deployment_id', deployment_id).execute()
        return deployment_logs.data
    
    def get_errors(self, deployment_id: int) -> Optional[list[DeploymentLogSchema]]:
        deployment_logs = supabase.table('deployment_logs').select().eq('deployment_id', deployment_id).eq('is_error', True).execute()
        return deployment_logs.data
    
deployment_log = CRUDDeploymentLog(DeploymentLog)