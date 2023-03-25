import os

from fastapi import FastAPI
from supabase import Client, create_client
from hubops_api.logger import setup_applevel_logger
from importlib import import_module

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
PUBLIC_SUPABASE_KEY = os.getenv('PUBLIC_SUPABASE_KEY')

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def register_routes(app: FastAPI):
    for file in os.listdir('hubops_api/routes'):
        if file.endswith('.py'):
            module = import_module(f'hubops_api.api.api_v1.endpoints.{file[:-3]}')
            app.include_router(module.router)

def create_app():
    app = FastAPI(
        __name__,
        title='HubOps API',
        description='API to allow for easier management of HubSpot environments'
    )
    setup_applevel_logger()
    return app