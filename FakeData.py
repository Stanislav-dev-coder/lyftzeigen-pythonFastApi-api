from pymongo import MongoClient
from faker import Faker
import random

# Создание экземпляра Faker
fake = Faker()

# Подключение к MongoDB
client = MongoClient("mongodb://mongodb.lyftzeigen.ru:28017/")
db = client['randomTest']
collection = db['indexRandomColletion']

def generate_fake_data(num_records):
    fake_data = []
    for _ in range(num_records):
        record = {
            "randomDateTime": fake.date_time_this_year(),
            "randomText": fake.text(),
            "randomNumber": fake.number(),
        }
        fake_data.append(record)
    return fake_data

num_records = 100  
fake_data = generate_fake_data(num_records)

collection.insert_many(fake_data)