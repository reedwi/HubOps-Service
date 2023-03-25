import logging
import sys

APP_LOGGER_NAME = 'HubOpsAPI'

def setup_applevel_logger(logger_name=APP_LOGGER_NAME, log_level=logging.DEBUG):
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(formatter)
    
    logger.handlers.clear()
    logger.addHandler(sh)
    
    return logger

def get_logger(module_name, logger_name=APP_LOGGER_NAME):
    return logging.getLogger(logger_name).getChild(module_name)