
"""
ChatGPT Service for handling OpenAI API interactions
"""
import logging
from typing import Optional
from openai import OpenAI

# Configure logging
logger = logging.getLogger(__name__)


class ChatGPTService:
    """Service class for interacting with ChatGPT API"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize ChatGPT service
        
        Args:
            api_key: OpenAI API key (placeholder: "YOUR_OPENAI_API_KEY_HERE")
        """
        self.model = "gpt-3.5-turbo"  # Default model
        
    def get_answer(self, question: str, model: Optional[str] = None) -> dict:
        """
        Send a question to ChatGPT and get the answer
        
        Args:
            question: The question to ask ChatGPT
            model: Optional model to use (default: gpt-3.5-turbo)
            
        Returns:
            dict: Response containing answer and metadata
            
        Raises:
            Exception: If API call fails
        """
        try:
            logger.info(f"Sending question to ChatGPT: {question[:100]}...")
            
            # Make API call to ChatGPT
            response = self.client.chat.completions.create(
                model=model or self.model,
                messages=[
                    {
                        "role": "user",
                        "content": question
                    }
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            # Extract answer from response
            answer = response.choices[0].message.content
            
            logger.info(f"Received answer from ChatGPT (length: {len(answer)} chars)")
            
            return {
                "success": True,
                "answer": answer,
                "model": response.model,
                "usage": {
                    "prompt_tokens": response.usage.prompt_tokens,
                    "completion_tokens": response.usage.completion_tokens,
                    "total_tokens": response.usage.total_tokens
                },
                "finish_reason": response.choices[0].finish_reason
            }
            
        except Exception as e:
            logger.error(f"Error calling ChatGPT API: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "answer": None
            }
    
    def set_api_key(self, api_key: str):
        """
        Update the API key
        
        Args:
            api_key: New OpenAI API key
        """
        self.api_key = api_key
        self.client = OpenAI(api_key=self.api_key)
        logger.info("API key updated")
    
    def set_model(self, model: str):
        """
        Update the default model
        
        Args:
            model: Model name (e.g., 'gpt-3.5-turbo', 'gpt-4')
        """
        self.model = model
        logger.info(f"Model updated to: {model}")


# Create a singleton instance
chatgpt_service = ChatGPTService()
