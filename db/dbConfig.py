from pymongo import MongoClient

client = MongoClient("MONGODB_URL")

db = client["rndDB"]

rndColIndex = db["rndColIndex"]
rndColNoIndex = db["rndColNoIndex"]
testCol = db["testCol"]
