import gc
from pymongo import MongoClient
from faker import Faker
import random

# Создание экземпляра Faker
fake = Faker()

# Подключение к MongoDB
client = MongoClient(
    "mongodb://mongoadmin:bdung@mongodb.lyftzeigen.ru:28017/")
db = client['rndDB']
# indexRandomCollection = db['rndColIndex']
# noIndexRandomCollection = db['rndColNoIndex']
testCol = db['testCol']


# print(collection.count_estimated_documents({}))

def generate_fake_data(num_records):
    fake_data = []
    for _ in range(num_records):
        record = {
            "randomDateTime": fake.date_time_this_year(),
            "randomText": fake.text(),
            "randomNumber": random.randint(42, 42000),
        }
        fake_data.append(record)
    return fake_data


def insert_large_amount_of_data(total_records, batch_size):
    for i in range(0, total_records, batch_size):
        batch_data = generate_fake_data(min(batch_size, total_records - i))
        # indexRandomCollection.insert_many(batch_data)
        testCol.insert_many(batch_data)
        print(f"Inserted batch {i // batch_size + 1}")
        del batch_data
        gc.collect()


total_records = 20
batch_size = 10

insert_large_amount_of_data(total_records, batch_size)
