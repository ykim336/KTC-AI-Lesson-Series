# Stage 1: ChatBot WITHOUT memory
import os
from simpleLLMP import SimpleLLMP

api_key = "..."

chatbot = SimpleLLMP()
chatbot.setup(api_key, "gpt-3.5-turbo")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    response = chatbot.generate(user_input)
    print(f"Bot: {response}")

