from hubops_api import create_app
from hubops_api.config import config_dict
import os

DEBUG = (os.getenv('DEBUG', 'False') == 'True')

config_mode = 'Debug' if DEBUG else 'Production'
app_config = config_dict[config_mode.capitalize()]

app = create_app()
