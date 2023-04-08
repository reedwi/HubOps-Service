from hubops_api.crud.base import CRUDBase
from typing import Optional
from hubops_api import supabase
from hubops_api.models.packages import PackageComponent
from hubops_api.schemas.packages import PackageComponentCreate 

class CRUDPackageComponent(CRUDBase[PackageComponent, PackageComponentCreate]):
    def get_components(self, package_id: int) -> Optional[PackageComponent]:
        components = supabase.table('package_components').select('*').eq('package_id', package_id).execute()
        return components.data
    
package_component = CRUDPackageComponent(PackageComponent)