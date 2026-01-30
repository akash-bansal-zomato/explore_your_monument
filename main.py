from flask import Flask, jsonify, render_template, send_from_directory
from model.monument import mongo  # Import the instance
import logging,os

# Import routers
# In main.py
from routers.health_router import health_bp
from routers.audio_router import audio_bp
from routers.admin_route import admin_bp

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config["MONGO_URI"] = "mongodb://localhost:27017/monumentDB"

# 2. Link the mongo instance to the app
mongo.init_app(app)

# Register blueprints
# app.register_blueprint(health_bp)
app.register_blueprint(audio_bp)
app.register_blueprint(admin_bp)

# Error handlers
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        "error": "Not found",
        "message": "The requested endpoint does not exist"
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        "error": "Internal server error",
        "message": "An unexpected error occurred"
    }), 500


@app.route('/')
def home():
    return render_template('index.html')


UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Add this route to serve images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

print(app.url_map)

if __name__ == "__main__":
    logger.info("Starting Audio Generation API...")
    app.run(host="0.0.0.0", port=8000, debug=True)
