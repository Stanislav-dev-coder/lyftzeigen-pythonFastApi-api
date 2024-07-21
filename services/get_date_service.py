from datetime import datetime
import pytz
import time


def get_date_service(collection, date: str):
    query_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f").replace(tzinfo=pytz.UTC)

    start_time = time.time()

    query = {"randomDateTime": query_date}
    explain_plan = collection.find(query).explain()
    end_time = time.time()
    execution_time = end_time - start_time
    print(explain_plan)

    # Извлечение данных из explain_plan
    execution_success = explain_plan.get("executionStats", {}).get("executionSuccess", False)
    execution_time_millis = explain_plan.get("executionStats", {}).get("executionTimeMillis")
    total_keys_examined = explain_plan.get("executionStats", {}).get("totalKeysExamined")

    return execution_success, execution_time_millis, total_keys_examined, execution_time
