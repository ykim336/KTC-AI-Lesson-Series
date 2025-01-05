# AI Chatbot Lesson Series (Scrapped)

Welcome to the AI Chatbot Lesson Series! This series will guide you through the process of creating an AI chatbot, optimizing it for better performance, and understanding different learning settings. By the end of this series, you'll have a solid understanding of how to build and enhance chatbots using modern AI techniques.

## Lesson 1: My First Chatbot

In this lesson, you will learn how to create a simple AI chatbot using the `SimpleLLMP` library. We'll cover the basics of setting up the chatbot, generating responses, and interacting with the user.

No Memory:
![Screenshot 2024-06-27 at 20 33 38](https://github.com/ykim336/KTC-AI-Lesson-Series/assets/117234817/df37533d-eec9-4376-b5fe-4e05493c3850)

Memory:
![Screenshot 2024-06-27 at 20 35 58](https://github.com/ykim336/KTC-AI-Lesson-Series/assets/117234817/35150f71-6e37-4f08-91b0-7695cd99b649)

### Objectives:
- Set up the `SimpleLLMP` library.
- Create a basic chatbot.
- Generate responses using the OpenAI API.
- Maintain conversation history.

### Steps:
1. **Set up the Environment**: Install required libraries and set up your API key.
2. **Create the `SimpleLLMP` Class**: Implement basic functionalities.
3. **Build the Chatbot**: Write a script to interact with the user.

### Example Code:
```python
# chatbot.py
import os
from simpleLLMP import SimpleLLMP

def main():
    api_key = "your-openai-api-key"

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

if __name__ == "__main__":
    main()
```

## Lesson 2: Better Chatbots With Optimization

This lesson focuses on optimizing your chatbot for better performance. We'll cover techniques like fine-tuning the model with custom data, enhancing response quality, and improving conversational flow.

### Objectives:
- Fine-tune the model with custom data.
- Optimize response generation.
- Maintain and enhance conversation history.

### Steps:
1. **Prepare Training Data**: Create a JSONL file with custom prompts and completions.
2. **Fine-Tune the Model**: Use the `SimpleLLMP` class to fine-tune the model.
3. **Update the Chatbot**: Enhance the chatbot to use the fine-tuned model.

Elsa [Frozen] Training Data:
```python
{"prompt": "what is love and marriage", "completion": "\"You can't marry a man you just met.\""}
{"prompt": "what is coming into her power", "completion": "\"I hear you. And I'm coming.\""}
{"prompt": "what on her accomplishments", "completion": "\"Here I am, I've come so far.\""}
{"prompt": "what on bonding with her sister", "completion": "\"Do you want to build a snowman?\""}
{"prompt": "opening herself (and her kingdom) up", "completion": "\"We're never closing them again.\""}
{"prompt": "acknowledging her strength", "completion": "\"Show yourself. Step into your power. Grow yourself into something new.\""}
{"prompt": "living without fear", "completion": "\"Let it go.\""}
```

Using this, we can train the chatbot to speak exactly how we want it to.
