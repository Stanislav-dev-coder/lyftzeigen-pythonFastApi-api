from fastapi import APIRouter
from models.randomDocument import RandomDocument
from db.dbConfig import rndColIndex, rndColNoIndex
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


@router.get("/getRndDocIndex")
async def get_rnd_doc_index_list():
    """
    GET first 10 docs from collection
    :return:
    """
    return list_serial(rndColIndex.find().limit(10))
