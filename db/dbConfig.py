from pymongo import MongoClient
import os

MONGODB_URL = os.environ.get("MONGODB_URL")
MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PASS = os.environ.get("MONGODB_PASS")
MONGODB_COLLECT = os.environ.get("MONGODB_COLLECT")

client = MongoClient(f"mongodb://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_URL}/{MONGODB_COLLECT}")

db = client["rndDB"]

rndColIndex = db["rndColIndex"]
rndColNoIndex = db["rndColNoIndex"]
testCol = db["testCol"]
