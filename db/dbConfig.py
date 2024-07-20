from pymongo import MongoClient
import os
from urllib.parse import quote_plus


MONGODB_URL = os.environ.get("MONGODB_URL")
MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PASS = os.environ.get("MONGODB_PASS")
MONGODB_COLLECT = os.environ.get("MONGODB_COLLECT")

uri = "mongodb://%s:%s@%s/%s" % (
    quote_plus(str(MONGODB_USER)), quote_plus(str(MONGODB_PASS)), quote_plus(str(MONGODB_URL)), quote_plus(str(MONGODB_COLLECT))
)

client = MongoClient(uri)

db = client["rndDB"]

rndColIndex = db["rndColIndex"]
rndColNoIndex = db["rndColNoIndex"]
testCol = db["testCol"]
