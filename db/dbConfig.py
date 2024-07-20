from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["rndDB"]

rndColIndex = db["rndColIndex"]
rndColNoIndex = db["rndColNoIndex"]
testCol = db["testCol"]
