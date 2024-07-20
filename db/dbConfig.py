from pymongo import MongoClient
import os

MONGODB_URL = os.environ.get("MONGODB_URL")
MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PASS = os.environ.get("MONGODB_PASS")

client = MongoClient(MONGODB_URL,
                     username=MONGODB_USER,
                     password=MONGODB_PASS)

db = client["rndDB"]

rndColIndex = db["rndColIndex"]
rndColNoIndex = db["rndColNoIndex"]
testCol = db["testCol"]
