from hubops_api.crud.base import CRUDBase
from hubops_api.models.packages import Package
from hubops_api.schemas.packages import PackageCreate

class CRUDPackage(CRUDBase[Package, PackageCreate]):
    pass

package = CRUDPackage(Package)