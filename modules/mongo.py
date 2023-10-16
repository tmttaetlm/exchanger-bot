import pymongo

def get_collection(name):
    db_client = pymongo.MongoClient("mongodb://localhost:27017/")
    current_db = db_client.currencydb
    collection = current_db[name]
    return collection
