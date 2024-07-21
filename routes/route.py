from fastapi import APIRouter, Query, HTTPException
from db.dbConfig import rndColIndex, rndColNoIndex, testCol
from services.get_date_service import get_date_service

router = APIRouter()


@router.get("/getIndexDate")
async def get_date_in_index_collection(date: str = Query(description="Date in ISO format (e.g., 2024-02-23T21:25:41.726000Z)")):
    try:
        (execution_success,
         execution_time_millis,
         total_keys_examined,
         execution_time) = get_date_service(rndColIndex, date)

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


@router.get("/getNoIndexDate")
async def get_date_in_noindex_collection(date: str = Query(description="Date in ISO format (e.g., 2024-02-23T21:25:41.726000Z)")):
    try:
        (execution_success,
         execution_time_millis,
         total_keys_examined,
         execution_time) = get_date_service(rndColNoIndex, date)

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
