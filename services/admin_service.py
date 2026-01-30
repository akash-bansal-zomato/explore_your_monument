import os
import uuid
import base64
from bson.objectid import ObjectId
from model.monument import mongo

class MonumentAdminService:
    @staticmethod
    def save_image(image_data):
        if not image_data or 'base64,' not in image_data:
            return image_data # Return existing URL if no new upload
        
        header, encoded = image_data.split(",", 1)
        data = base64.b64decode(encoded)
        filename = f"{uuid.uuid4()}.jpg"
        filepath = os.path.join('uploads', filename)
        
        with open(filepath, 'wb') as f:
            f.write(data)
        return f"/uploads/{filename}"

    @staticmethod
    def save_monument_group(data):
        mon_id = data.get('id')
        
        # Process each location in the array
        processed_locations = []
        for loc in data.get('locations', []):
            img_url = loc.get('image_url')
            # If a new image was uploaded in this session
            if loc.get('image_data'):
                img_url = MonumentAdminService.save_image(loc['image_data'])
            
            processed_locations.append({
                "id": loc.get('id') or str(uuid.uuid4()),
                "name": loc.get('name'),
                "lat": float(loc.get('lat')),
                "lng": float(loc.get('lng')),
                "question": loc.get('question'),
                "image_url": img_url
            })

        doc = {
            "monument_name": data['monument_name'],
            "locations": processed_locations
        }

        if mon_id:
            mongo.db.monuments.update_one({"_id": ObjectId(mon_id)}, {"$set": doc})
            return mon_id
        else:
            result = mongo.db.monuments.insert_one(doc)
            return str(result.inserted_id)

    @staticmethod
    def get_all_groups():
        groups = list(mongo.db.monuments.find())
        for g in groups:
            g['_id'] = str(g['_id'])
        return groups