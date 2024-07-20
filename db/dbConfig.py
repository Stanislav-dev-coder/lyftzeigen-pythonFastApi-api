from pymongo import MongoClient
import os

# MONGODB_HOST = "mongodb.lyftzeigen.ru"
# MONGODB_PORT = "28017"
# MONGODB_USER = "testUser"
# MONGODB_PASS = "root1234"
# MONGODB_AUTH_DB = "rndDB"

MONGODB_HOST = os.environ.get("MONGODB_HOST")
MONGODB_PORT = os.environ.get("MONGODB_PORT")
MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PASS = os.environ.get("MONGODB_PASS")
MONGODB_AUTH_DB = os.environ.get("MONGODB_AUTH_DB")

client = MongoClient(f"mongodb://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_HOST}:{MONGODB_PORT}/?directConnection=true&authSource={MONGODB_AUTH_DB}")

db = client["rndDB"]

rndColIndex = db["rndColIndex"]
rndColNoIndex = db["rndColNoIndex"]
testCol = db["testCol"]
