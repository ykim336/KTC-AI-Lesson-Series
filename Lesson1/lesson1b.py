# Stage 2: ChatBot WITH memory
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
    chatbot.add_to_history("user", user_input)
    chatbot.add_to_history("assistant", response)
