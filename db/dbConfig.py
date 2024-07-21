from pymongo import MongoClient
from urllib.parse import quote_plus
import os

MONGODB_HOST = os.environ.get("MONGODB_HOST")
MONGODB_PORT = os.environ.get("MONGODB_PORT")
MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PASS = os.environ.get("MONGODB_PASS")
MONGODB_AUTH_DB = os.environ.get("MONGODB_AUTH_DB")

uri = "mongodb://%s:%s@%s:%s/?authSource=%s" % (
    quote_plus(MONGODB_USER), quote_plus(MONGODB_PASS), quote_plus(MONGODB_HOST), quote_plus(MONGODB_PORT), quote_plus(MONGODB_AUTH_DB)
)

client = MongoClient(uri)

db = client["rndDB"]

rndColIndex = db["rndColIndex"]
rndColNoIndex = db["rndColNoIndex"]
testCol = db["testCol"]
