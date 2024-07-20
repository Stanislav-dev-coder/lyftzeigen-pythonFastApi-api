from pymongo import MongoClient
from envparse import Env

env = Env()
MONGODB_URL = env.str("MONGODB_URL")

client = MongoClient("mongodb://mongoadmin:bdung@mongodb.lyftzeigen.ru:28017/")

db = client["rndDB"]

rndColIndex = db["rndColIndex"]
rndColNoIndex = db["rndColNoIndex"]
testCol = db["testCol"]
