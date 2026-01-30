from bson.objectid import ObjectId
from model.monument import mongo

class MonumentAdminService:
    """
    Handles all administrative operations for Monuments.
    """
    
    @staticmethod
    def get_monument_list():
        # Fetch only necessary fields for the admin dropdown
        cursor = mongo.db.monuments.find({}, {"name": 1, "location": 1, "question": 1})
        monuments = list(cursor)
        for m in monuments:
            m['_id'] = str(m['_id'])
        return monuments

    @staticmethod
    def create_monument(data):
        # Business Logic: Ensure GeoJSON format is strictly followed
        document = {
            "name": data['name'],
            "question": data['question'],
            "location": {
                "type": "Point",
                "coordinates": [float(data['lng']), float(data['lat'])]
            },
            "updated_at": "2026-01-30" # Track admin changes
        }
        result = mongo.db.monuments.insert_one(document)
        return str(result.inserted_id)

    @staticmethod
    def update_existing_monument(mon_id, data):
        update_doc = {
            "name": data['name'],
            "question": data['question'],
            "location": {
                "type": "Point",
                "coordinates": [float(data['lng']), float(data['lat'])]
            }
        }
        mongo.db.monuments.update_one(
            {'_id': ObjectId(mon_id)}, 
            {'$set': update_doc}
        )
        return True

    @staticmethod
    def delete_monument(mon_id):
        mongo.db.monuments.delete_one({'_id': ObjectId(mon_id)})