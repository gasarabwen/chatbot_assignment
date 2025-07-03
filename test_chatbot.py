#!/usr/bin/env python3

from chatbot import ask_chatbot

if __name__ == "__main__":
    print("Testing chatbot...")
    try:
        response = ask_chatbot("How do I apply for admission?")
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error occurred: {e}")
        import traceback
        traceback.print_exc()
