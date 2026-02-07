#!/usr/bin/env python3
"""
Example script demonstrating GPT4All usage for quick testing.

This script shows a simple one-shot query to the GPT4All model
without entering the interactive chat mode.
"""

from gpt4all import GPT4All


def quick_query(question):
    """
    Perform a quick query to the GPT4All model.
    
    Args:
        question (str): The question to ask the model
    
    Returns:
        str: The model's response
    """
    print("Loading GPT4All model...")
    try:
        model = GPT4All("mistral-7b-openorca.gguf2.Q4_0.gguf")
    except Exception:
        # Fallback to default model
        model = GPT4All()
    
    print("Generating response...\n")
    
    with model.chat_session():
        response = model.generate(question, max_tokens=200)
    
    return response


if __name__ == "__main__":
    # Example question
    question = "What is the capital of France?"
    
    print(f"Question: {question}\n")
    answer = quick_query(question)
    print(f"Answer: {answer}")
