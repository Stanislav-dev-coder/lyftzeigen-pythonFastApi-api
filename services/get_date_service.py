from datetime import datetime
import pytz
import time


def get_date_service(collection, count: int):

    start_time = time.time()
    explain_plan = collection.find().limit(count).sort("randomDateTime", 1).explain()
    end_time = time.time()
    execution_time = end_time - start_time
    print(explain_plan)

    execution_success = explain_plan.get("executionStats", {}).get("executionSuccess", False)
    execution_time_millis = explain_plan.get("executionStats", {}).get("executionTimeMillis")
    total_keys_examined = explain_plan.get("executionStats", {}).get("totalKeysExamined")

    return execution_success, execution_time_millis, total_keys_examined, execution_time
