from pymongo import MongoClient
try:
    client = MongoClient('127.0.0.1', 27017)
except:
    print("Connection failed")

database = client['SKRIPSI_LSTM']
collection = database['PRICE']
cursor = collection.find()

for record in cursor:
    print(record)