from pymongo import MongoClient
import os
from urllib.parse import quote_plus


#MONGODB_URL = os.environ.get("MONGODB_URL")
#$MONGODB_USER = os.environ.get("MONGODB_USER")
#MONGODB_PASS = os.environ.get("MONGODB_PASS")
#MONGODB_COLLECT = os.environ.get("MONGODB_COLLECT")

MONGODB_HOST = "mongodb.lyftzeigen.ru"
MONGODB_PORT = 28017
MONGODB_USER = "testUser"
MONGODB_PASS = "root1234"  # Замените "root1234" на ваш реальный пароль
MONGODB_AUTH_DB = "rndDB"

# Формируем строку подключения
uri = "mongodb://%s:%s@%s:%s/?authSource=%s" % (
    quote_plus(MONGODB_USER), quote_plus(MONGODB_PASS), quote_plus(MONGODB_HOST), MONGODB_PORT, quote_plus(MONGODB_AUTH_DB)
)

client = MongoClient(uri)

db = client["rndDB"]

rndColIndex = db["rndColIndex"]
rndColNoIndex = db["rndColNoIndex"]
testCol = db["testCol"]
