# AI-Powered Code Generator

An intelligent code generation tool powered by OpenAI's GPT-4 API that enables developers to automatically generate, explain, and save code in multiple programming languages through an intuitive Gradio interface.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-green.svg)
![Gradio](https://img.shields.io/badge/Gradio-UI-orange.svg)

## 🌟 Features

- **Multi-Language Support**: Generate code in Python, JavaScript, and Java
- **Intelligent Code Explanation**: Get clear, simple explanations of generated code
- **Copy to Clipboard**: One-click functionality to copy generated code
- **Save to File**: Download generated code with custom filenames
- **User-Friendly Interface**: Clean, intuitive Gradio web interface
- **Real-Time Generation**: Fast code generation powered by GPT-4

## 🚀 Live Demo

[View Live Demo](https://your-deployed-app.onrender.com) *(Add your Render URL here)*

## 📸 Screenshots

![Code Generator Interface](screenshot.png) *(Optional: Add a screenshot)*

## 🛠️ Technologies Used

- **Python 3.7+**
- **OpenAI GPT-4 API** - Advanced language model for code generation
- **Gradio** - Interactive web interface framework
- **Python-dotenv** - Environment variable management

## 📋 Prerequisites

Before you begin, ensure you have:

- Python 3.7 or higher installed
- An OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- pip package manager

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rtollinchi/AI-powered-code-generator-.git
   cd AI-powered-code-generator-
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the root directory:
   ```bash
   touch .env
   ```

   Add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## 🎮 Usage

1. **Run the application**
   ```bash
   python app.py
   ```

2. **Open your browser**

   The app will automatically open, or navigate to:
   ```
   http://localhost:7860
   ```

3. **Generate code**
   - Select your desired programming language (Python, JavaScript, or Java)
   - Enter a description of what you want the code to do
   - Click "Generate Code"
   - Copy or save the generated code

## 💡 Example Use Cases

- **Quick Prototyping**: Generate boilerplate code for new projects
- **Learning Tool**: Understand how to implement specific algorithms
- **Code Translation**: Convert logic between different programming languages
- **Documentation**: Generate code examples with explanations

## 📁 Project Structure

```
AI-powered-code-generator-/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (not in repo)
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## 🔐 Security Note

**Important**: Never commit your `.env` file or expose your OpenAI API key. The `.gitignore` file should include:

```
.env
__pycache__/
*.pyc
.venv/
venv/
```

## 🌐 Deployment

This app is deployed on [Render](https://render.com). To deploy your own instance:

1. Fork this repository
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Add environment variable: `OPENAI_API_KEY`
5. Use these settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`

## 👤 Author

**Rubin Tollinchi**

- GitHub: [@Rtollinchi](https://github.com/Rtollinchi)
- LinkedIn: [Your LinkedIn](https://www.linkedin.com/in/rubintollinchi/)
- Portfolio: [Your Website](https://rubintollinchi.info/)

## 🙏 Acknowledgments

- OpenAI for providing the GPT-4 API
- Gradio team for the excellent UI framework
- The open-source community

## 📞 Support

If you have any questions or run into issues, please open an issue in the GitHub repository.

---

⭐ If you found this project helpful, please consider giving it a star!
