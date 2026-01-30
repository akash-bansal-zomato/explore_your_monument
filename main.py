
from flask import Flask, request, jsonify, send_file
from models import AudioRequest
from pydantic import ValidationError
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route("/", methods=['GET'])
def root():
    """Root endpoint - API health check"""
    return jsonify({
        "message": "Audio Generation API is running",
        "status": "healthy",
        "version": "1.0.0"
    })


@app.route("/generate-audio", methods=['POST'])
def generate_audio():
    """
    Generate audio from text question
    
    Request Body:
        AudioRequest containing requestId, userId, and question
        
    Returns:
        Audio file (placeholder for now)
    """
    try:
        # Validate request data using Pydantic model
        try:
            audio_request = AudioRequest(**request.get_json())
        except ValidationError as e:
            logger.error(f"Validation error: {e}")
            return jsonify({
                "error": "Invalid request data",
                "details": e.errors()
            }), 400
        
        logger.info(f"Received request: requestId={audio_request.requestId}, userId={audio_request.userId}")
        logger.info(f"Question: {audio_request.question}")
        
        # TODO: Implement actual audio generation logic here
        # For now, return a JSON response acknowledging the request
        # Once audio generation is implemented, this will return send_file with audio file
        
        return jsonify({
            "message": "Audio generation endpoint (logic to be implemented)",
            "requestId": audio_request.requestId,
            "userId": audio_request.userId,
            "question": audio_request.question,
            "status": "pending_implementation",
            "note": "Audio file will be generated and returned here"
        }), 200
        
        # Example of how to return audio file once generation is implemented:
        # audio_file_path = generate_audio_file(audio_request.question)
        # return send_file(
        #     audio_file_path,
        #     mimetype="audio/mpeg",
        #     as_attachment=True,
        #     download_name=f"audio_{audio_request.requestId}.mp3"
        # )
        
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({
            "error": "Error generating audio",
            "detail": str(e)
        }), 500


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

