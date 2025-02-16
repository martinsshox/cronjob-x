from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Env:
    DISCLOUD_BASE_URL: str = getenv("DISCLOUD_BASE_URL")
    DISCLOUD_API_TOKEN: str = getenv("DISCLOUD_API_TOKEN")
    DISCORD_WEBHOOK_URL_DEBUG: str = getenv("DISCORD_WEBHOOK_URL_DEBUG")
    DISCORD_WEBHOOK_URL_WARNING: str = getenv("DISCORD_WEBHOOK_URL_WARNING")
    DISCORD_WEBHOOK_URL_ERROR: str = getenv("DISCORD_WEBHOOK_URL_ERROR")