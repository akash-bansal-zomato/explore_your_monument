"""
Routers package initialization
"""
from .health_router import health_bp
from .audio_router import audio_bp

__all__ = ['health_bp', 'audio_bp']
