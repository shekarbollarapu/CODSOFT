# Rule-based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there! What can I do for you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I am a chatbot created to assist you. You can call me ChatBot!",
        "help": "Sure, I'm here to help. What do you need assistance with?",
        "bye": "Goodbye! Have a nice day!",
        "default": "I'm sorry, I don't understand that. Can you please rephrase?"
    }
    
    for key in responses:
        if key in user_input:
            return responses[key]
    
    return responses["default"]

# Chatbot loop
def chat():
    print("ChatBot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye! Have a nice day!")
            break
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chat()
