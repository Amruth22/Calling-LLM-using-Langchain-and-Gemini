"""
Main application for the Simple Text Generator using LangChain and Gemini
Provides an interactive menu system for different text generation options
"""

from services.gemini_service import GeminiService
from util.config import Config
from exception.generation_exceptions import APIKeyException, GenerationException, InvalidInputException
import os
import time

def print_header():
    """Print the application header"""
    print("\n" + "="*50)
    print("=== Simple Text Generator with Gemini ===")
    print("="*50 + "\n")

def print_menu():
    """Display the main menu"""
    print("1. Generate simple text")
    print("2. Generate with style")
    print("3. Generate creative content")
    print("4. Exit")
    print()

def generate_simple(service):
    """Handle simple text generation"""
    print("\n--- Generate Simple Text ---")
    prompt = input("Enter your prompt: ")
    
    print("\nGenerating text...")
    time.sleep(1)  # Show loading effect
    
    try:
        response = service.generate_simple_text(prompt)
        print("\nGenerated Text:")
        print("-" * 40)
        print(response.content)
        print("-" * 40)
    except Exception as e:
        print(f"\nError: {e}")

def generate_with_style(service):
    """Handle styled text generation"""
    print("\n--- Generate with Style ---")
    topic = input("Enter topic: ")
    print("\nChoose style:")
    print("1. Formal")
    print("2. Casual")
    print("3. Funny")
    
    style_choice = input("Enter choice (1-3): ")
    styles = {"1": "formal", "2": "casual", "3": "funny"}
    
    if style_choice not in styles:
        print("Invalid style choice!")
        return
    
    style = styles[style_choice]
    
    print(f"\nGenerating {style} text about {topic}...")
    time.sleep(1)
    
    try:
        response = service.generate_with_template(topic, style)
        print("\nGenerated Text:")
        print("-" * 40)
        print(response.content)
        print("-" * 40)
    except Exception as e:
        print(f"\nError: {e}")

def generate_creative(service):
    """Handle creative content generation"""
    print("\n--- Generate Creative Content ---")
    print("Content types:")
    print("1. Poem")
    print("2. Story")
    print("3. Joke")
    print("4. Fun Fact")
    
    type_choice = input("Choose type (1-4): ")
    types = {"1": "poem", "2": "story", "3": "joke", "4": "fact"}
    
    if type_choice not in types:
        print("Invalid choice!")
        return
    
    content_type = types[type_choice]
    subject = input(f"Enter subject for your {content_type}: ")
    
    print(f"\nGenerating {content_type} about {subject}...")
    time.sleep(1)
    
    try:
        response = service.generate_creative_content(content_type, subject)
        print(f"\nGenerated {content_type.title()}:")
        print("-" * 40)
        print(response.content)
        print("-" * 40)
    except Exception as e:
        print(f"\nError: {e}")

def main():
    """Main program function"""
    print_header()
    
    # Get API key
    try:
        api_key = Config.get_api_key()
    except APIKeyException:
        print("No API key found in environment variables.")
        print("\nTo get your free API key:")
        print("1. Go to https://aistudio.google.com/app/apikey")
        print("2. Sign in with Google")
        print("3. Click 'Create API Key'")
        print()
        api_key = input("Enter your Gemini API key: ")
        
        if not Config.validate_api_key(api_key):
            print("Invalid API key format!")
            return
    
    # Initialize service
    try:
        print("Initializing Gemini service...")
        service = GeminiService(api_key)
        print("Service ready!\n")
    except Exception as e:
        print(f"Failed to initialize service: {e}")
        return
    
    # Main loop
    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            generate_simple(service)
        elif choice == '2':
            generate_with_style(service)
        elif choice == '3':
            generate_creative(service)
        elif choice == '4':
            print("\nThank you for using Text Generator!")
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice! Please try again.")
        
        if choice in ['1', '2', '3']:
            input("\nPress Enter to continue...")
            print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nUnexpected error: {e}")