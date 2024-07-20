from pymongo import MongoClient
import os

MONGODB_URL = os.environ.get("MONGODB_URL")
MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PASS = os.environ.get("MONGODB_PASS")
MONGODB_COLLECT = os.environ.get("MONGODB_COLLECT")

client = MongoClient(
        MONGODB_URL,
        username=MONGODB_USER,
        password=MONGODB_PASS,
        authSource=MONGODB_COLLECT,
        authMechanism='SCRAM-SHA-256'
)

db = client["rndDB"]

rndColIndex = db["rndColIndex"]
rndColNoIndex = db["rndColNoIndex"]
testCol = db["testCol"]
