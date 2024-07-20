from fastapi import APIRouter
from models.randomDocument import RandomDocument
from db.dbConfig import rndColIndex, rndColNoIndex, testCol
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


@router.get("/getAllTestCol")
async def get_test_doc_list():
    """
    GET first 10 docs from collection
    :return:
    """
    return list_serial(testCol.find().limit(10))
