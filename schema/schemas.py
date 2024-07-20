def individual_serial(rnd_doc) -> dict:
    return {
        "id": str(rnd_doc["_id"]),
        "randomDateTime": rnd_doc["randomDateTime"],
        "randomText": rnd_doc["randomText"],
        "randomNumber": int(rnd_doc["randomNumber"]),
    }


def list_serial(rnd_doc_list) -> list:
    return [individual_serial(rnd_doc) for rnd_doc in rnd_doc_list]