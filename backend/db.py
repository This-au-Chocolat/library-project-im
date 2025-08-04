from pymongo import MongoClient

client = MongoClient("mongodb+srv://rivaldo:12345@cluster0.kb8gjbn.mongodb.net/")
db = client['library_db']
books_collection = db['books']