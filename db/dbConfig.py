from pymongo import MongoClient

client = MongoClient("mongodb://mongoadmin:bdung@mongodb.lyftzeigen.ru:28017/")

db = client["rndDB"]

rndColIndex = db["rndColIndex"]
rndColNoIndex = db["rndColNoIndex"]
testCol = db["testCol"]
