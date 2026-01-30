from flask import Blueprint, request, jsonify
from services.admin_service import MonumentAdminService

admin_bp = Blueprint('admin', __name__,url_prefix='/admin')

@admin_bp.route('/monuments', methods=['GET'])
def list_monuments():
    data = MonumentAdminService.get_monument_list()
    return jsonify(data)

@admin_bp.route('/monuments', methods=['POST'])
def save_monument():
    data = request.json
    mon_id = data.get('id')
    
    if mon_id:
        MonumentAdminService.update_existing_monument(mon_id, data)
        return jsonify({"message": "Updated successfully"})
    else:
        new_id = MonumentAdminService.create_monument(data)
        return jsonify({"message": "Created successfully", "id": new_id})

@admin_bp.route('/monuments/<id>', methods=['DELETE'])
def remove_monument(id):
    MonumentAdminService.delete_monument(id)
    return jsonify({"message": "Deleted successfully"})