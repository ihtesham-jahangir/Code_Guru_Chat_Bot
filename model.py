import google.generativeai as genai
import os
import time
from typing import Any

# Configure Gemini API with your Google API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

class MessageItem:
    def __init__(self, role: str, content: str | Any):
        self.role: str = role
        self.content: str | Any = content   

class GoogleGenerativeAIBot:
    def __init__(self, name: str, instructions: str) -> None:
        self.name: str = name
        self.instructions: str = instructions
        self.thread: int = 1  # Dummy thread ID, adjust as needed
        self.messages: list[MessageItem] = []

    def send_message(self, message: str):
        self.add_message("user: " + message)

    def generate_response(self, user_input: str) -> MessageItem:
        response = model.generate_content(user_input)
        message = MessageItem("bot", response)
        self.add_message(message)
        return message

    def get_messages(self) -> list[MessageItem]:
        return self.messages

    def add_message(self, message: MessageItem) -> None:
        self.messages.append(message)

# Initialize the Gemini Pro model
model = genai.GenerativeModel('gemini-pro')


