from motor.motor_asyncio import AsyncIOMotorClient
import requests
from config import *

from ..logging import LOGGER



LOGGER(__name__).info("Connecting to your Mongo Database...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    s = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getme?")
    x = s.json()
    if x["ok"]:
        username = x["result"]["username"]
    else:
        username = "zohary"
    mongodb = _mongo_async_[username]
    LOGGER(__name__).info(f"Connected to your {username} Mongo Database.")
except:
    LOGGER(__name__).error("Failed to connect to your Mongo Database.")
    exit()
