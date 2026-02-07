#!/usr/bin/env python3
"""
GPT4All Offline Model Application

This application allows you to run GPT4All models completely offline.
It provides an interactive chat interface to communicate with the AI model.
"""

import sys
from gpt4all import GPT4All


def main():
    """Main function to run the GPT4All offline model."""
    print("=" * 60)
    print("GPT4All Offline Model Application")
    print("=" * 60)
    print()
    
    # Initialize the model
    print("Initializing GPT4All model...")
    print("Note: On first run, the model will be downloaded automatically.")
    print("This may take a few minutes depending on your internet speed.")
    print()
    
    try:
        # Using the recommended mistral model (default)
        model = GPT4All("mistral-7b-openorca.gguf2.Q4_0.gguf")
        print("Model loaded successfully!")
        print()
    except Exception as e:
        print(f"Error loading model: {e}")
        print()
        print("Trying to use the default model instead...")
        try:
            model = GPT4All()
            print("Default model loaded successfully!")
            print()
        except Exception as e2:
            print(f"Error loading default model: {e2}")
            print("Please ensure you have an internet connection for first-time model download.")
            sys.exit(1)
    
    print("=" * 60)
    print("Chat Interface")
    print("=" * 60)
    print("Type your messages below. Type 'exit', 'quit', or press Ctrl+C to end.")
    print()
    
    # Interactive chat loop
    conversation_history = []
    
    try:
        while True:
            # Get user input
            user_input = input("You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("\nGoodbye!")
                break
            
            # Skip empty inputs
            if not user_input:
                continue
            
            # Add user message to conversation history
            conversation_history.append({"role": "user", "content": user_input})
            
            # Generate response
            print("AI: ", end="", flush=True)
            
            with model.chat_session():
                response = model.generate(user_input, max_tokens=200, streaming=True)
                full_response = ""
                for token in response:
                    print(token, end="", flush=True)
                    full_response += token
                print()  # New line after response
            
            # Add assistant response to conversation history
            conversation_history.append({"role": "assistant", "content": full_response})
            print()
            
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
