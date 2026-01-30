from flask import Blueprint, request, jsonify
from services.admin_service import MonumentAdminService

admin_bp = Blueprint('admin', __name__,url_prefix='/admin')

@admin_bp.route('/monuments', methods=['GET'])
def list_monuments():
    return jsonify(MonumentAdminService.get_all_groups())

@admin_bp.route('/monuments', methods=['POST'])
def save_monument():
    res = MonumentAdminService.save_monument_group(request.json)
    return jsonify({"id": res, "status": "success"})

@admin_bp.route('/monuments/<id>', methods=['DELETE'])
def delete_monument(id):
    from models.monument import mongo
    from bson.objectid import ObjectId
    mongo.db.monuments.delete_one({"_id": ObjectId(id)})
    return jsonify({"status": "deleted"})