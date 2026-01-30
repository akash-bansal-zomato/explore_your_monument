"""
Health check router
"""
from flask import Blueprint, jsonify

health_bp = Blueprint('health', __name__)


@health_bp.route("/", methods=['GET'])
def root():
    """Root endpoint - API health check"""
    return jsonify({
        "message": "Audio Generation API is running",
        "status": "healthy",
        "version": "1.0.0"
    })
