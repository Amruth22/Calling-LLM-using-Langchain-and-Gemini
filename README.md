# 🤖 Simple Text Generator using LangChain and Gemini

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)
![Gemini](https://img.shields.io/badge/Gemini-2.0%20Flash-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Beginner Friendly](https://img.shields.io/badge/Beginner-Friendly-brightgreen.svg)

**🎯 Learn AI Integration • 🚀 Build with LangChain • 🆓 Use Free Gemini API**

</div>

---

## 📖 Table of Contents

- [🌟 What is This Project?](#-what-is-this-project)
- [🎓 What You'll Learn](#-what-youll-learn)
- [🔑 Getting Your Free API Key](#-getting-your-free-api-key)
- [📁 Project Structure Explained](#-project-structure-explained)
- [🛠️ Setup Instructions](#️-setup-instructions)
- [🚀 How to Run](#-how-to-run)
- [✨ Features Overview](#-features-overview)
- [📝 Code Walkthrough](#-code-walkthrough)
- [🧪 Testing](#-testing)
- [💡 Tips for Beginners](#-tips-for-beginners)
- [🔧 Troubleshooting](#-troubleshooting)
- [🎯 Next Steps](#-next-steps)

---

## 🌟 What is This Project?

This is a **beginner-friendly project** that teaches you how to integrate **Google's Gemini AI** with **LangChain** framework to create a text generator. Think of it as your first step into the world of AI programming!

### 🎯 **Perfect for:**
- 👨‍💻 **Beginners** learning AI integration
- 🎓 **Students** studying machine learning
- 🚀 **Developers** exploring LangChain
- 🔬 **Anyone** curious about AI APIs

### 🆓 **Why This Project?**
- **100% Free** - Uses Google's free Gemini API
- **No Complex Setup** - Simple Python project
- **Real AI Integration** - Not just theory, actual working code
- **Well Documented** - Every line explained

---

## 🎓 What You'll Learn

By completing this project, you'll understand:

| 📚 **Concept** | 🎯 **What You'll Master** |
|----------------|---------------------------|
| **🔑 API Integration** | How to connect to Google's Gemini AI |
| **🦜 LangChain Framework** | Using LangChain for AI model interaction |
| **🏗️ Project Structure** | Organizing Python projects professionally |
| **⚠️ Error Handling** | Managing API errors gracefully |
| **🧪 Testing** | Writing tests for your code |
| **🔧 Configuration** | Managing API keys securely |

---

## 🔑 Getting Your Free API Key

### 📋 **Step-by-Step Guide:**

1. **🌐 Visit Google AI Studio**
   ```
   👉 Go to: https://aistudio.google.com/app/apikey
   ```

2. **🔐 Sign In**
   - Use your Google account (Gmail, etc.)
   - No special account needed!

3. **🆕 Create API Key**
   - Click the **"Create API Key"** button
   - Choose **"Create API key in new project"**

4. **💾 Save Your Key**
   - **Copy** the key immediately
   - **Store it safely** (we'll use it later)
   - **Never share it publicly!**

### 🎁 **What You Get for Free:**
- ✅ **60 requests per minute**
- ✅ **Gemini 2.0 Flash model** (fastest!)
- ✅ **No credit card required**
- ✅ **Perfect for learning**

---

## 📁 Project Structure Explained

Let's break down every file and folder so you understand exactly what each part does:

```
📦 Calling-LLM-using-Langchain-and-Gemini/
├── 📄 README.md                    # 👈 You are here! Project documentation
├── 📄 requirements.txt             # 📦 List of Python packages we need
├── 📄 main.py                      # 🚀 Main program - run this to start!
├── 📄 tests.py                     # 🧪 Tests to make sure everything works
├── 📄 .env.example                 # 📝 Example of how to set up your API key
├── 📄 .gitignore                   # 🚫 Files Git should ignore
│
├── 📁 model/                       # 🏗️ Data structures (how we organize information)
│   ├── 📄 __init__.py             # 🐍 Makes this folder a Python package
│   └── 📄 text_generation.py      # 📝 Classes for requests and responses
│
├── 📁 services/                    # 🔧 Business logic (the main work happens here)
│   ├── 📄 __init__.py             # 🐍 Makes this folder a Python package
│   └── 📄 gemini_service.py       # 🤖 Connects to Gemini AI using LangChain
│
├── 📁 util/                        # 🛠️ Utility functions (helper tools)
│   ├── 📄 __init__.py             # 🐍 Makes this folder a Python package
│   └── 📄 config.py               # ⚙️ Manages settings and API keys
│
└── 📁 exception/                   # ⚠️ Custom error handling
    ├── 📄 __init__.py             # 🐍 Makes this folder a Python package
    └── 📄 generation_exceptions.py # 🚨 Custom error messages
```

### 🔍 **Detailed File Explanations:**

#### 📄 **main.py** - The Heart of Our Application
```python
# This is where everything starts!
# Contains:
# - Interactive menu system
# - User input handling
# - Calls to our AI service
# - Pretty output formatting
```

#### 🏗️ **model/text_generation.py** - Data Structures
```python
# Contains two important classes:

class TextRequest:
    # Represents what the user wants to generate
    # - prompt: What they want to write about
    # - max_length: How long the response should be
    # - temperature: How creative the AI should be

class TextResponse:
    # Represents the AI's response
    # - content: The generated text
    # - model_used: Which AI model was used
    # - timestamp: When it was created
```

#### 🤖 **services/gemini_service.py** - AI Integration
```python
# This is where the magic happens!
# Contains the GeminiService class that:
# - Connects to Google's Gemini AI
# - Uses LangChain framework
# - Handles different types of text generation
# - Manages AI model settings
```

#### ⚙️ **util/config.py** - Configuration Management
```python
# Handles all the settings:
# - Loading API keys from environment variables
# - Default values for AI parameters
# - Validation of API keys
# - Security best practices
```

#### ⚠️ **exception/generation_exceptions.py** - Error Handling
```python
# Custom error messages for common problems:
# - APIKeyException: When API key is missing
# - GenerationException: When AI generation fails
# - InvalidInputException: When user input is wrong
```

---

## 🛠️ Setup Instructions

### 📋 **Prerequisites:**
- 🐍 **Python 3.8 or higher** ([Download here](https://python.org))
- 💻 **Command line/Terminal access**
- 🌐 **Internet connection**
- 🔑 **Google account** (for API key)

### 🚀 **Step 1: Clone the Repository**
```bash
# Download the project
git clone https://github.com/Amruth22/Calling-LLM-using-Langchain-and-Gemini.git

# Enter the project folder
cd "Calling-LLM-using-Langchain-and-Gemini"
```

### 🏠 **Step 2: Create Virtual Environment**
```bash
# Create a virtual environment (recommended!)
python -m venv venv

# Activate it:
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate

# You should see (venv) in your terminal now!
```

> 💡 **Why virtual environment?** It keeps this project's packages separate from your other Python projects!

### 📦 **Step 3: Install Dependencies**
```bash
# Install all required packages
pip install -r requirements.txt

# This installs:
# - langchain-google-genai (for Gemini integration)
# - langchain (the main framework)
# - python-dotenv (for environment variables)
# - pytest (for testing)
```

### 🔑 **Step 4: Set Up Your API Key**

**🎯 Method 1: Environment Variable (Recommended)**
```bash
# Windows:
set GEMINI_API_KEY=your-actual-api-key-here

# Mac/Linux:
export GEMINI_API_KEY=your-actual-api-key-here
```

**🎯 Method 2: .env File**
```bash
# Copy the example file
cp .env.example .env

# Edit .env file and add your key:
# GEMINI_API_KEY=your-actual-api-key-here
```

---

## 🚀 How to Run

### 🎮 **Starting the Application:**
```bash
# Make sure you're in the project folder
python main.py
```

### 🎯 **What You'll See:**
```
==================================================
=== Simple Text Generator with Gemini ===
==================================================

Initializing Gemini service...
Service ready!

1. Generate simple text
2. Generate with style
3. Generate creative content
4. Exit

Enter your choice (1-4): 
```

### 🎪 **Interactive Demo:**

**🔹 Option 1: Simple Text Generation**
```
--- Generate Simple Text ---
Enter your prompt: What is artificial intelligence?

Generating text...

Generated Text:
----------------------------------------
Artificial Intelligence (AI) is like giving computers 
the ability to think and learn like humans. It's 
technology that can recognize patterns, make decisions, 
and solve problems without being explicitly programmed 
for every single task.
----------------------------------------
```

**🔹 Option 2: Styled Text Generation**
```
--- Generate with Style ---
Enter topic: Python programming
Choose style:
1. Formal
2. Casual  
3. Funny

Enter choice (1-3): 3

Generating funny text about Python programming...

Generated Text:
----------------------------------------
Python programming is like having a conversation with 
a very literal friend who does exactly what you say, 
even if you accidentally tell them to print "Hello World" 
a million times. It's the programming language that's 
more friendly than a golden retriever! 🐍
----------------------------------------
```

**🔹 Option 3: Creative Content**
```
--- Generate Creative Content ---
Content types:
1. Poem
2. Story
3. Joke
4. Fun Fact

Choose type (1-4): 1
Enter subject for your poem: Ocean

Generating poem about Ocean...

Generated Poem:
----------------------------------------
Waves whisper secrets to the shore,
Deep blue mysteries and so much more,
Endless horizon where sky meets sea,
Ocean's rhythm sets my spirit free.
----------------------------------------
```

---

## ✨ Features Overview

### 🎯 **Core Features:**

| 🌟 **Feature** | 📝 **Description** | 🎮 **How to Use** |
|----------------|-------------------|-------------------|
| **Simple Generation** | Ask any question, get AI response | Choose option 1, type your question |
| **Styled Writing** | Generate formal, casual, or funny text | Choose option 2, pick a style |
| **Creative Content** | Generate poems, stories, jokes, facts | Choose option 3, pick content type |
| **Error Handling** | Graceful error messages | Automatic - handles API issues |
| **Secure API Management** | Safe API key handling | Set environment variable |

### 🔧 **Technical Features:**

- **🦜 LangChain Integration**: Professional AI framework
- **⚡ Gemini 2.0 Flash**: Google's fastest AI model
- **🛡️ Error Handling**: Custom exceptions for different scenarios
- **🧪 Testing Suite**: Comprehensive tests included
- **📦 Modular Design**: Clean, organized code structure
- **🔒 Security**: API keys never stored in code

---

## 📝 Code Walkthrough

Let's understand the key parts of our code:

### 🤖 **How AI Integration Works:**

```python
# In services/gemini_service.py
from langchain_google_genai import ChatGoogleGenerativeAI

class GeminiService:
    def __init__(self, api_key):
        # This creates our connection to Gemini
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",    # Google's fastest model
            google_api_key=api_key,      # Your API key
            temperature=0.7,             # Creativity level
            max_output_tokens=200        # Response length limit
        )
    
    def generate_simple_text(self, prompt):
        # This sends your prompt to Gemini and gets response
        response = self.llm.invoke(prompt)
        return TextResponse(response.content)
```

### 🏗️ **How Data is Structured:**

```python
# In model/text_generation.py
class TextRequest:
    def __init__(self, prompt, max_length=100, temperature=0.7):
        self.prompt = prompt           # What user wants to generate
        self.max_length = max_length   # How long the response should be
        self.temperature = temperature # How creative (0.0 = focused, 1.0 = creative)

class TextResponse:
    def __init__(self, content, model_used="gemini-2.0-flash"):
        self.content = content         # The AI-generated text
        self.model_used = model_used   # Which AI model was used
        self.timestamp = datetime.now() # When it was created
```

### ⚠️ **How Errors are Handled:**

```python
# In exception/generation_exceptions.py
class APIKeyException(Exception):
    # Thrown when API key is missing or invalid
    def __init__(self, message="API key is missing or invalid..."):
        super().__init__(message)

class GenerationException(Exception):
    # Thrown when AI generation fails
    def __init__(self, message="Failed to generate text..."):
        super().__init__(message)
```

### 🎮 **How the Menu System Works:**

```python
# In main.py
def main():
    # Get API key
    api_key = Config.get_api_key()
    
    # Initialize AI service
    service = GeminiService(api_key)
    
    # Main menu loop
    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            generate_simple(service)    # Simple text generation
        elif choice == '2':
            generate_with_style(service) # Styled generation
        elif choice == '3':
            generate_creative(service)   # Creative content
        elif choice == '4':
            break                       # Exit program
```

---

## 🧪 Testing

### 🔍 **Why Testing Matters:**
Testing ensures our code works correctly and helps catch bugs early!

### 🚀 **Run All Tests:**
```bash
# Run the complete test suite
python -m pytest tests.py -v

# Expected output:
# ✅ test_model_folder_exists PASSED
# ✅ test_text_request_creation PASSED
# ✅ test_gemini_service_import PASSED
# ... and many more!
```

### 🧩 **What Our Tests Check:**

| 🧪 **Test Category** | 📋 **What It Tests** |
|----------------------|----------------------|
| **📁 Structure Tests** | All folders and files exist |
| **🏗️ Model Tests** | TextRequest and TextResponse classes work |
| **⚠️ Exception Tests** | Error handling works correctly |
| **⚙️ Config Tests** | Configuration management works |
| **📦 Import Tests** | All modules can be imported |

### 🔧 **Run Specific Tests:**
```bash
# Test only the model classes
python -m pytest tests.py::test_text_request_creation -v

# Test only file structure
python -m pytest tests.py -k "folder_exists" -v
```

---

## 💡 Tips for Beginners

### 🎯 **Getting Started:**

1. **🐣 Start Simple**
   ```
   Try prompts like:
   - "Explain photosynthesis in simple terms"
   - "Write a short paragraph about cats"
   - "What is the capital of France?"
   ```

2. **🎨 Experiment with Creativity**
   ```
   Temperature settings:
   - 0.0 = Very focused, same results
   - 0.7 = Balanced (default)
   - 1.0 = Very creative, different each time
   ```

3. **📝 Try Different Styles**
   ```
   Same topic, different styles:
   - Formal: "Machine learning is a subset of artificial intelligence..."
   - Casual: "So machine learning is basically teaching computers..."
   - Funny: "Machine learning is like training a very smart pet computer..."
   ```

### 🔧 **Best Practices:**

- **💾 Save Your API Key**: Set it as environment variable
- **📊 Monitor Usage**: Check your usage at Google AI Studio
- **🔄 Try Multiple Times**: Same prompt can give different results
- **📏 Adjust Length**: Use max_length parameter for longer/shorter responses
- **🛡️ Handle Errors**: Always wrap API calls in try-catch blocks

### 🚀 **Advanced Tips:**

- **🎭 Use Templates**: Create reusable prompt templates
- **📚 Chain Prompts**: Use output from one prompt as input to another
- **🎯 Be Specific**: More specific prompts give better results
- **🔍 Experiment**: Try different models and parameters

---

## 🔧 Troubleshooting

### 🚨 **Common Issues and Solutions:**

#### ❌ **"API key is missing or invalid"**
```bash
# Solution 1: Check environment variable
echo $GEMINI_API_KEY  # Mac/Linux
echo %GEMINI_API_KEY% # Windows

# Solution 2: Verify your API key
# Go to https://aistudio.google.com/app/apikey
# Make sure you copied the full key

# Solution 3: Set it again
export GEMINI_API_KEY=your-key-here  # Mac/Linux
set GEMINI_API_KEY=your-key-here     # Windows
```

#### ❌ **"Failed to generate text"**
```bash
# Possible causes:
# 1. Internet connection issue
# 2. API rate limit exceeded (60 requests/minute)
# 3. Invalid prompt

# Solutions:
# - Check internet connection
# - Wait a minute and try again
# - Try a simpler prompt
```

#### ❌ **"Module not found" errors**
```bash
# Make sure virtual environment is activated
# You should see (venv) in your terminal

# Reinstall dependencies
pip install -r requirements.txt

# Check Python version
python --version  # Should be 3.8+
```

#### ❌ **"Permission denied" errors**
```bash
# On Mac/Linux, you might need:
chmod +x main.py

# Or run with python explicitly:
python main.py
```

### 🆘 **Getting Help:**

1. **📖 Check the error message** - it usually tells you what's wrong
2. **🔍 Google the error** - someone else probably had the same issue
3. **📚 Read the documentation** - LangChain and Gemini docs are helpful
4. **💬 Ask for help** - Create an issue in this repository

---

## 🎯 Next Steps

### 🚀 **Enhance This Project:**

1. **🎨 Add More Features:**
   ```python
   # Ideas to implement:
   - Conversation history
   - Different AI models
   - Text-to-speech output
   - Web interface with Flask
   - Database to save generations
   ```

2. **🌐 Create a Web Version:**
   ```python
   # Use Flask or FastAPI to create:
   - Web interface
   - REST API endpoints
   - User authentication
   - Generation history
   ```

3. **📱 Build a Mobile App:**
   ```python
   # Use frameworks like:
   - Kivy (Python mobile apps)
   - React Native (with Python backend)
   - Flutter (with Python API)
   ```

### 📚 **Learn More About:**

- **🦜 LangChain**: [Official Documentation](https://python.langchain.com/)
- **🤖 Google Gemini**: [Gemini API Docs](https://ai.google.dev/)
- **🐍 Python Best Practices**: [PEP 8 Style Guide](https://pep8.org/)
- **🧪 Testing**: [Pytest Documentation](https://docs.pytest.org/)
- **🔧 API Design**: [REST API Best Practices](https://restfulapi.net/)

### 🎓 **Related Projects to Try:**

1. **Chatbot with Memory** - Build a conversational AI
2. **Document Summarizer** - Summarize long texts
3. **Code Generator** - Generate code from descriptions
4. **Language Translator** - Translate between languages
5. **Content Moderator** - Check text for inappropriate content

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🎯 **Ways to Contribute:**

- 🐛 **Report Bugs**: Found an issue? Create an issue!
- ✨ **Suggest Features**: Have an idea? We'd love to hear it!
- 📝 **Improve Documentation**: Help make this README even better!
- 🧪 **Add Tests**: More tests = more reliable code!
- 🎨 **Add Features**: Implement new functionality!

### 📋 **Contribution Guidelines:**

1. **🍴 Fork the repository**
2. **🌿 Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **💾 Commit your changes**: `git commit -m 'Add amazing feature'`
4. **📤 Push to branch**: `git push origin feature/amazing-feature`
5. **🔄 Open a Pull Request**

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### 🎁 **What this means:**
- ✅ **Free to use** for personal and commercial projects
- ✅ **Free to modify** and distribute
- ✅ **No warranty** - use at your own risk
- ✅ **Attribution appreciated** but not required

---

## 🙏 Acknowledgments

- **🤖 Google** for providing the free Gemini API
- **🦜 LangChain** team for the amazing framework
- **🐍 Python** community for excellent libraries
- **👥 Open Source** community for inspiration

---
