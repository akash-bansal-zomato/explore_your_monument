from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Initialize PyMongo without the app first (Factory Pattern)
mongo = PyMongo()

class MonumentModel:
    """
    Data Access Layer for Monuments in MongoDB.
    This keeps raw DB queries out of your service logic.
    """
    
    @staticmethod
    def find_all():
        return list(mongo.db.monuments.find())

    @staticmethod
    def find_by_id(mon_id):
        return mongo.db.monuments.find_one({"_id": ObjectId(mon_id)})

    @staticmethod
    def insert(data):
        return mongo.db.monuments.insert_one(data)

    @staticmethod
    def update(mon_id, data):
        return mongo.db.monuments.update_one(
            {"_id": ObjectId(mon_id)}, 
            {"$set": data}
        )

    @staticmethod
    def delete(mon_id):
        return mongo.db.monuments.delete_one({"_id": ObjectId(mon_id)})