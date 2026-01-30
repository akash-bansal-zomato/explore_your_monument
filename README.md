
# Audio Generation API

A simple and manageable Flask application for generating audio from text questions.

## Project Structure

```
.
├── main.py           # Flask application and endpoints
├── models.py         # Pydantic models for request validation
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## Setup Instructions

1. **Create and activate virtual environment** (if not already done):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```
   
   Or using Flask directly:
   ```bash
   flask --app main run --host 0.0.0.0 --port 8000
   ```

## API Endpoints

### Health Check
- **Endpoint**: `GET /`
- **Description**: Check if the API is running
- **Response**:
  ```json
  {
    "message": "Audio Generation API is running",
    "status": "healthy",
    "version": "1.0.0"
  }
  ```

### Generate Audio
- **Endpoint**: `POST /generate-audio`
- **Description**: Generate audio from text question (logic to be implemented)
- **Request Body**:
  ```json
  {
    "requestId": "req_123456",
    "userId": "user_789",
    "question": "What is the weather today?"
  }
  ```
- **Response** (current placeholder):
  ```json
  {
    "message": "Audio generation endpoint (logic to be implemented)",
    "requestId": "req_123456",
    "userId": "user_789",
    "question": "What is the weather today?",
    "status": "pending_implementation",
    "note": "Audio file will be generated and returned here"
  }
  ```

## Testing the API

Using curl:
```bash
curl -X POST "http://localhost:8000/generate-audio" \
  -H "Content-Type: application/json" \
  -d '{
    "requestId": "req_123456",
    "userId": "user_789",
    "question": "What is the weather today?"
  }'
```

Using Python requests:
```python
import requests

response = requests.post(
    "http://localhost:8000/generate-audio",
    json={
        "requestId": "req_123456",
        "userId": "user_789",
        "question": "What is the weather today?"
    }
)
print(response.json())
```

## Future Implementation

The audio generation logic will be added later. When implemented, the `/generate-audio` endpoint will:
1. Process the question text
2. Generate audio file
3. Return the audio file as a downloadable response

The endpoint is already structured to return a file response with the audio file once the generation logic is complete.
