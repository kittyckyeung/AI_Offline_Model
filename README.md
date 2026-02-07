# AI Offline Model - GPT4All Application

A simple, user-friendly application for running GPT4All models completely offline. This app provides an interactive chat interface to communicate with AI models locally, ensuring privacy and offline functionality.

## Features

- 🔒 **Complete Offline Operation**: Once the model is downloaded, the app runs entirely offline
- 💬 **Interactive Chat Interface**: Simple command-line interface for chatting with the AI
- 🚀 **Easy Setup**: Just install dependencies and run
- 🔐 **Privacy-Focused**: All data stays on your local machine
- 🤖 **Powered by GPT4All**: Uses high-quality open-source language models

## Prerequisites

- Python 3.8 or higher
- Internet connection (only for initial model download)
- At least 4GB of free disk space for the model

## Installation

1. Clone this repository:
```bash
git clone https://github.com/kittyckyeung/AI_Offline_Model.git
cd AI_Offline_Model
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python app.py
```

On first run, the application will automatically download the AI model (this may take a few minutes). After the initial download, the app will work completely offline.

### Chat Commands

- Type your message and press Enter to chat with the AI
- Type `exit`, `quit`, or `q` to end the session
- Press `Ctrl+C` to interrupt and exit

### Example Session

```
============================================================
GPT4All Offline Model Application
============================================================

Initializing GPT4All model...
Note: On first run, the model will be downloaded automatically.
This may take a few minutes depending on your internet speed.

Model loaded successfully!

============================================================
Chat Interface
============================================================
Type your messages below. Type 'exit', 'quit', or press Ctrl+C to end.

You: Hello! What can you help me with?
AI: Hello! I'm an AI assistant. I can help you with various tasks such as:
- Answering questions
- Providing information
- Helping with writing and editing
- Solving problems
- And much more!

What would you like assistance with today?

You: exit
Goodbye!
```

## Technical Details

### Model Information

The application uses the GPT4All framework, which provides access to various open-source language models optimized for local execution. By default, it attempts to use the Mistral-7B model, which offers a good balance of performance and resource usage.

### System Requirements

- **RAM**: Minimum 8GB recommended
- **Storage**: At least 4GB free space for model files
- **CPU**: Multi-core processor recommended for better performance
- **OS**: Windows, macOS, or Linux

## Troubleshooting

**Model download fails:**
- Ensure you have a stable internet connection
- Check that you have sufficient disk space
- The model will be stored in your user's home directory under `.cache/gpt4all/`

**Application runs slowly:**
- This is normal on first interaction as the model loads into memory
- Consider using a computer with more RAM for better performance
- Close other memory-intensive applications

**Error on startup:**
- Make sure Python 3.8+ is installed: `python --version`
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Check that the gpt4all package is properly installed: `pip show gpt4all`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project uses GPT4All, which is licensed under the MIT License. Please refer to the GPT4All project for specific licensing information.

## Acknowledgments

- [GPT4All](https://github.com/nomic-ai/gpt4all) - The underlying framework for running LLMs locally
- All contributors to open-source language models

## Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.