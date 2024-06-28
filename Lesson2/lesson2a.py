import os
from simpleLLMP import SimpleLLMP


api_key = "..."
chatbot = SimpleLLMP()
chatbot.setup(api_key, "gpt-3.5-turbo")

training_file_path = 'datasets/elsa.jsonl'
model_name = chatbot.fine_tune_model(training_file_path)
print(f"Fine-tuned model name: {model_name}")

