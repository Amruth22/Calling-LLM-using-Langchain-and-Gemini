"""Custom exceptions for text generation operations"""

class APIKeyException(Exception):
    """Raised when API key is missing or invalid"""
    
    def __init__(self, message="API key is missing or invalid. Please check your Gemini API key."):
        super().__init__(message)

class GenerationException(Exception):
    """Raised when text generation fails"""
    
    def __init__(self, message="Failed to generate text. Please try again."):
        super().__init__(message)

class InvalidInputException(Exception):
    """Raised when user input is invalid"""
    
    def __init__(self, message="Invalid input. Please provide a valid prompt."):
        super().__init__(message)