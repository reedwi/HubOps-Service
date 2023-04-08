from hubops_api.logger import get_logger
from fastapi import APIRouter, status
from hubops_api import supabase
from hubops_api import schemas, crud
from typing import Optional
import os
import requests

router = APIRouter(prefix='/packages')

logger = get_logger(__name__)

@router.get('/all', response_model=list[schemas.Package])
def get_packages(
    current_user: schemas.User # Need to figure out auth mechanism with in deps
) -> Optional[list[schemas.Package]]:
    packages = crud.package.get_many()
    return packages



@router.get('/{id}', response_model=schemas.Package)
def get_package(id: int) -> Optional[schemas.Package]:
    package = crud.package.get(id=id)
    return package



@router.post('/create', response_model=schemas.Package)
def create_package(
    package: schemas.PackageCreate
) -> Optional[schemas.Package]:
    new_package = crud.package.create(package)
    return new_package



@router.delete('/{id}', response_model=None)
def delete_package(id: int) -> None:
    crud.package.delete(id=id)
    return None



@router.post('/{id}/deployment', response_model=schemas.PackageDeployment)
def create_deployment(
    id: int,
    deployment: schemas.PackageDeploymentCreate
) -> Optional[schemas.PackageDeployment]:
    new_deployment = crud.package_deployment.create(deployment)
    return new_deployment



@router.get('/{id}/deployment/{deployment_id}', response_model=schemas.PackageDeployment)
def get_deployment(
    id: int,
    deployment_id: int) -> Optional[schemas.PackageDeployment]:
    deployment = crud.package_deployment.get(id=deployment_id)
    return deployment



@router.put('/{id}/deployment/{deployment_id}', response_model=schemas.PackageDeployment)
def update_deployment(
    id: int,
    deployment_id: int,
    deployment: schemas.PackageDeploymentUpdate
) -> Optional[schemas.PackageDeployment]:
    updated_deployment = crud.package_deployment.update(deployment_id, deployment)
    return updated_deployment



@router.get('/{id}/deployment/{deployment_id}', response_model=list[schemas.DeploymentLog])
def get_deployment_logs(
    id: int,
    deployment_id: int
) -> Optional[list[schemas.DeploymentLog]]:
    logs = crud.deployment_log.get_logs(deployment_id=deployment_id)
    return logs



@router.get('/{id}/deployment/{deployment_id}/errors', response_model=list[schemas.DeploymentLog])
def get_deployment_errors(
    id: int,
    deployment_id: int
) -> Optional[list[schemas.DeploymentLog]]:
    logs = crud.deployment_log.get_errors(deployment_id=deployment_id)
    return logs