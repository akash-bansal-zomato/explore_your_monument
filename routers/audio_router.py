"""
Audio generation router
"""
from flask import Blueprint, request, jsonify, send_file
from models import AudioRequest
from services import monument_service
from pydantic import ValidationError
import logging

# Configure logging
logger = logging.getLogger(__name__)

audio_bp = Blueprint('audio', __name__)


@audio_bp.route("/generate-audio", methods=['POST'])
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
        
        # Call Monument Service to process the question
        monument_result = monument_service.process_question(
            question=audio_request.question,
            request_id=audio_request.requestId,
            user_id=audio_request.userId
        )
        
        logger.info(f"Monument service processing status: {monument_result.get('status')}")
        
        # TODO: Use monument_result for audio generation when logic is complete
        # TODO: Implement actual audio generation logic here
        
        return jsonify({
            "message": "Request processed by Monument Service",
            "requestId": audio_request.requestId,
            "userId": audio_request.userId,
            "question": audio_request.question,
            "monument_status": monument_result.get('status'),
            "status": "pending_implementation",
            "note": "Monument service received the question. Audio generation logic to be added."
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
