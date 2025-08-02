"""
Test suite for the Simple Text Generator project
Tests file structure, model classes, and basic functionality
"""

import os
import pytest
from model.text_generation import TextRequest, TextResponse
from exception.generation_exceptions import APIKeyException, InvalidInputException, GenerationException

# Test if all directories exist
def test_model_folder_exists():
    """Test that the model directory exists"""
    assert os.path.isdir("model"), "Directory 'model' is missing!"

def test_services_folder_exists():
    """Test that the services directory exists"""
    assert os.path.isdir("services"), "Directory 'services' is missing!"

def test_util_folder_exists():
    """Test that the util directory exists"""
    assert os.path.isdir("util"), "Directory 'util' is missing!"

def test_exception_folder_exists():
    """Test that the exception directory exists"""
    assert os.path.isdir("exception"), "Directory 'exception' is missing!"

# Test if all files exist
def test_text_generation_file_exists():
    """Test that text_generation.py exists"""
    assert os.path.isfile("model/text_generation.py"), "File 'text_generation.py' is missing!"

def test_gemini_service_file_exists():
    """Test that gemini_service.py exists"""
    assert os.path.isfile("services/gemini_service.py"), "File 'gemini_service.py' is missing!"

def test_config_file_exists():
    """Test that config.py exists"""
    assert os.path.isfile("util/config.py"), "File 'config.py' is missing!"

def test_exceptions_file_exists():
    """Test that generation_exceptions.py exists"""
    assert os.path.isfile("exception/generation_exceptions.py"), "File 'generation_exceptions.py' is missing!"

def test_main_file_exists():
    """Test that main.py exists"""
    assert os.path.isfile("main.py"), "File 'main.py' is missing!"

def test_requirements_file_exists():
    """Test that requirements.txt exists"""
    assert os.path.isfile("requirements.txt"), "File 'requirements.txt' is missing!"

# Test model classes
def test_text_request_creation():
    """Test TextRequest class creation and attributes"""
    request = TextRequest("Test prompt", 50, 0.5)
    assert request.prompt == "Test prompt"
    assert request.max_length == 50
    assert request.temperature == 0.5

def test_text_request_defaults():
    """Test TextRequest class with default values"""
    request = TextRequest("Test prompt")
    assert request.prompt == "Test prompt"
    assert request.max_length == 100
    assert request.temperature == 0.7

def test_text_request_str():
    """Test TextRequest string representation"""
    request = TextRequest("Test prompt", 50, 0.5)
    str_repr = str(request)
    assert "Test prompt" in str_repr
    assert "50" in str_repr
    assert "0.5" in str_repr

def test_text_response_creation():
    """Test TextResponse class creation and attributes"""
    response = TextResponse("Generated content")
    assert response.content == "Generated content"
    assert response.model_used == "gemini-2.0-flash"
    assert response.timestamp is not None

def test_text_response_custom_model():
    """Test TextResponse with custom model name"""
    response = TextResponse("Generated content", "custom-model")
    assert response.content == "Generated content"
    assert response.model_used == "custom-model"

def test_text_response_str():
    """Test TextResponse string representation"""
    response = TextResponse("Generated content")
    str_repr = str(response)
    assert "Generated content" in str_repr
    assert "gemini-2.0-flash" in str_repr

# Test exception classes
def test_api_key_exception():
    """Test APIKeyException creation"""
    with pytest.raises(APIKeyException) as exc_info:
        raise APIKeyException()
    assert "API key is missing or invalid" in str(exc_info.value)

def test_generation_exception():
    """Test GenerationException creation"""
    with pytest.raises(GenerationException) as exc_info:
        raise GenerationException()
    assert "Failed to generate text" in str(exc_info.value)

def test_invalid_input_exception():
    """Test InvalidInputException creation"""
    with pytest.raises(InvalidInputException) as exc_info:
        raise InvalidInputException()
    assert "Invalid input" in str(exc_info.value)

def test_custom_exception_messages():
    """Test custom exception messages"""
    custom_message = "Custom error message"
    
    with pytest.raises(APIKeyException) as exc_info:
        raise APIKeyException(custom_message)
    assert custom_message in str(exc_info.value)

# Test configuration
def test_config_import():
    """Test that Config class can be imported"""
    from util.config import Config
    assert Config is not None

def test_config_constants():
    """Test Config class constants"""
    from util.config import Config
    assert hasattr(Config, 'DEFAULT_MAX_LENGTH')
    assert hasattr(Config, 'DEFAULT_TEMPERATURE')
    assert hasattr(Config, 'DEFAULT_MODEL')
    assert Config.DEFAULT_MAX_LENGTH == 100
    assert Config.DEFAULT_TEMPERATURE == 0.7
    assert Config.DEFAULT_MODEL == "gemini-2.0-flash"

# Test service import
def test_gemini_service_import():
    """Test that GeminiService class can be imported"""
    from services.gemini_service import GeminiService
    assert GeminiService is not None

# Integration tests (these would require actual API key)
def test_project_structure_complete():
    """Test that all required files and directories are present"""
    required_files = [
        "main.py",
        "requirements.txt",
        "README.md",
        "tests.py",
        "model/__init__.py",
        "model/text_generation.py",
        "services/__init__.py", 
        "services/gemini_service.py",
        "util/__init__.py",
        "util/config.py",
        "exception/__init__.py",
        "exception/generation_exceptions.py"
    ]
    
    for file_path in required_files:
        assert os.path.isfile(file_path), f"Required file '{file_path}' is missing!"

if __name__ == "__main__":
    # Run tests if script is executed directly
    pytest.main([__file__, "-v"])