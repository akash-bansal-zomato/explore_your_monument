from pydantic import BaseModel, Field


class AudioRequest(BaseModel):
    """Request model for audio generation"""
    requestId: str = Field(..., description="Unique request identifier")
    userId: str = Field(..., description="User identifier")
    question: str = Field(..., description="Question text for audio generation")

    class Config:
        json_schema_extra = {
            "example": {
                "requestId": "req_123456",
                "userId": "user_789",
                "question": "What is the weather today?"
            }
        }
