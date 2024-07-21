from fastapi import APIRouter, Query, HTTPException
from db.dbConfig import rndColIndex, rndColNoIndex, testCol
from services.get_date_service import get_date_service

router = APIRouter()


@router.get("/testIndexCollection")
async def test_index_collection(count: int):
    try:
        (execution_success,
         execution_time_millis,
         total_keys_examined,
         execution_time) = get_date_service(rndColIndex, count)

        return {
            "executionSuccess": execution_success,
            "executionTimeMillis": execution_time_millis,
            "totalKeysExamined": total_keys_examined,
            "executionPythonTme": execution_time
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid date format: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/testNoIndexCollection")
async def test_no_index_collection(count: int):
    try:
        (execution_success,
         execution_time_millis,
         total_keys_examined,
         execution_time) = get_date_service(rndColNoIndex, count)

        return {
            "executionSuccess": execution_success,
            "executionTimeMillis": execution_time_millis,
            "totalKeysExamined": total_keys_examined,
            "executionPythonTme": execution_time
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid date format: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
