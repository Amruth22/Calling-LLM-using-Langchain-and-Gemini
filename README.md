# Simple Text Generator using LangChain and Gemini

Learn how to call Google's Gemini AI model using LangChain framework. This beginner project teaches you the basics of connecting to AI models and generating text based on user prompts. We'll use Google's free Gemini API which is perfect for learning.

## What You'll Learn

- How to get a free Google Gemini API key
- How to use LangChain to call Gemini API
- How to create different types of prompts
- Basic error handling in Python

## Getting Your Free Gemini API Key

1. **Go to Google AI Studio**: Visit https://aistudio.google.com/app/apikey
2. **Sign in**: Use your Google account to sign in
3. **Create API Key**: Click "Create API Key" button
4. **Save your key**: Copy and save your API key safely (never share it!)

**Note**: The free tier gives you 60 requests per minute which is plenty for learning! We're using Gemini 2.0 Flash which is Google's fastest and most efficient model.

## Project Structure

```
TextGenerator/
├── model/
│   └── text_generation.py      # Data models for requests and responses
├── services/
│   └── gemini_service.py       # LangChain integration with Gemini
├── util/
│   └── config.py               # Configuration and API key management
├── exception/
│   └── generation_exceptions.py # Custom exception classes
├── main.py                     # Main application
├── tests.py                    # Test cases
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## How to Set Up Your Environment

### 1. Create a virtual environment:
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### 2. Install required packages:
```bash
pip install -r requirements.txt
```

### 3. Set your API key (choose one method):

**Method 1 - Environment Variable (Recommended):**
```bash
# On Windows:
set GEMINI_API_KEY=your-api-key-here

# On Mac/Linux:
export GEMINI_API_KEY=your-api-key-here
```

**Method 2 - .env file:**
Create a file named `.env` in your project:
```
GEMINI_API_KEY=your-api-key-here
```

## How to Run the Project

1. Navigate to project folder:
```bash
cd "Calling LLM using Langchain and Gemini"
```

2. Run the program:
```bash
python main.py
```

## Sample Program Flow

```
=== Simple Text Generator with Gemini ===
1. Generate simple text
2. Generate with style
3. Generate creative content
4. Exit

Enter your choice: 1

--- Generate Simple Text ---
Enter your prompt: Explain what machine learning is in simple terms

Generating text...

Generated Text:
--------------
Machine learning is like teaching a computer to learn from examples, 
just like how you learned to recognize cats and dogs by seeing many 
pictures of them. Instead of programming exact rules, we show the 
computer lots of examples and it figures out the patterns by itself.

Press Enter to continue...
```

## Features

### 1. Simple Text Generation
- Enter any prompt and get AI-generated text
- Perfect for questions, explanations, or creative writing

### 2. Styled Text Generation
- Choose from formal, casual, or funny styles
- Great for different writing contexts

### 3. Creative Content Generation
- Generate poems, stories, jokes, or fun facts
- Explore AI's creative capabilities

## Tips for Beginners

1. **Start Small**: Try simple prompts first before complex ones
2. **Experiment with Temperature**:
   - 0.0 = Very focused, predictable
   - 0.7 = Balanced (default)
   - 1.0 = Very creative, random
3. **Save Your API Key**: Set it as environment variable so you don't need to enter it each time
4. **Monitor Usage**: Free tier has limits, check your usage at https://aistudio.google.com
5. **Try Different Prompts**: The same prompt can give different results each time

## Common Errors and Solutions

- **"API key is missing"**: Make sure you set the GEMINI_API_KEY environment variable
- **"Connection error"**: Check your internet connection
- **"Rate limit exceeded"**: Free tier allows 60 requests/minute, wait a bit and try again
- **"Invalid API key"**: Double-check your key from Google AI Studio

## Testing

Run the test suite to verify everything is working:
```bash
python -m pytest tests.py -v
```

## Contributing

Feel free to fork this project and add your own features! Some ideas:
- Add more content types
- Implement conversation history
- Add text-to-speech output
- Create a web interface

## License

This project is open source and available under the MIT License.