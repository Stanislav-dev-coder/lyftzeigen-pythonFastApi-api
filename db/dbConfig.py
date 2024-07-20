from pymongo import MongoClient
import os

MONGODB_URL = os.environ.get("MONGODB_URL")

client = MongoClient(MONGODB_URL)

db = client["rndDB"]

rndColIndex = db["rndColIndex"]
rndColNoIndex = db["rndColNoIndex"]
testCol = db["testCol"]
