from hubops_api.crud.base import CRUDBase
from hubops_api.models.packages import PackageDeployment
from hubops_api.schemas.packages import PackageDeploymentCreate, PackageDeploymentUpdate

class CRUDPackageDeployment(CRUDBase[PackageDeployment, PackageDeploymentCreate, PackageDeploymentUpdate]):
    pass 

package_deployment = CRUDPackageDeployment(PackageDeployment)