from fastapi import APIRouter, Query, HTTPException
from models.randomDocument import RandomDocument
from db.dbConfig import rndColIndex, rndColNoIndex, testCol
from schema.schemas import list_serial
from bson import ObjectId
import time
from datetime import datetime
import pytz

router = APIRouter()


@router.get("/getIndexDate")
async def get_test_doc_list(date: str = Query(..., description="Date in ISO format (e.g., 2024-02-23T21:25:41.726000Z)")):
    """
    GET first 10 docs from test collection
    :return: list of docs
    """
    try:
        # Преобразуем строку даты в объект datetime
        query_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f").replace(tzinfo=pytz.UTC)

        start_time = time.time()

        # Выполняем запрос с объяснением
        query = {"randomDateTime": query_date}
        explain_plan = rndColIndex.find(query).explain()

        end_time = time.time()
        execution_time = end_time - start_time

        # Возвращаем результаты и время выполнения
        return {
            "explainPlan": explain_plan,
            "executionTimeSeconds": execution_time
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid date format: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/getNoIndexDate")
async def get_test_doc_list(date: str = Query(..., description="Date in ISO format (e.g., 2024-02-23T21:25:41.726000Z)")):
    """
    GET first 10 docs from test collection
    :return: list of docs
    """
    try:
        # Преобразуем строку даты в объект datetime
        query_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f").replace(tzinfo=pytz.UTC)

        start_time = time.time()

        # Выполняем запрос с объяснением
        query = {"randomDateTime": query_date}
        explain_plan = rndColNoIndex.find(query).explain()

        end_time = time.time()
        execution_time = end_time - start_time

        # Возвращаем результаты и время выполнения
        return {
            "explainPlan": explain_plan,
            "executionTimeSeconds": execution_time
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid date format: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
