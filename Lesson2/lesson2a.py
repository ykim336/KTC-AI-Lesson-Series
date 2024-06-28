import os
from simpleLLMP import SimpleLLMP


api_key = "sk-proj-9vr7tGRvmJHAZkwmBGq8T3BlbkFJ4TnFuGSmRJxzPSOuP4yM"
# chatbot = SimpleLLMP()
# chatbot.setup(api_key, "gpt-3.5-turbo")

# training_file_path = 'datasets/elsa.jsonl'
# model_name = chatbot.fine_tune_model(training_file_path)
# print(f"Fine-tuned model name: {model_name}")

model_name = "ft:davinci-002:yvon-kim:elsa:9ewK68xR"
chatbot = SimpleLLMP()
chatbot.setup(api_key, model_name)

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    response = chatbot.generate(user_input)
    print(f"Elsa: {response}")

