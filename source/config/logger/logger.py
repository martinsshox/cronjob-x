import logging
from ..Env import Env
from .LevelFilter import LevelFilter
from .WebhookHandler import WebhookHandler

LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

def setup_logger():

    logger = logging.getLogger("JobAppLogger")
    logger.setLevel(logging.DEBUG)  
    logger.propagate = False

    formatter = logging.Formatter(LOG_FORMAT)

    debug_handler = WebhookHandler(Env.DISCORD_WEBHOOK_URL_DEBUG)
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(formatter)
    debug_handler.addFilter(LevelFilter(logging.DEBUG))

    warning_handler = WebhookHandler(Env.DISCORD_WEBHOOK_URL_WARNING)
    warning_handler.setLevel(logging.WARNING)
    warning_handler.setFormatter(formatter)
    warning_handler.addFilter(LevelFilter(logging.WARNING))

    error_handler = WebhookHandler(Env.DISCORD_WEBHOOK_URL_ERROR)
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)
    error_handler.addFilter(LevelFilter(logging.ERROR))

    logger.addHandler(debug_handler)
    logger.addHandler(warning_handler)
    logger.addHandler(error_handler)

    return logger

logger = setup_logger()