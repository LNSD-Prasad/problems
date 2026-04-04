# Basic Chatbot using Python

print("Chatbot: Hello! I am your chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Chatbot: Hi there!")
    
    elif user_input == "how are you":
        print("Chatbot: I am fine! How can I help you?")
    
    elif user_input == "your name":
        print("Chatbot: I am a simple chatbot.")
    
    elif user_input == "bye":
        print("Chatbot: Goodbye!")
        break
    
    else:
        print("Chatbot: Sorry, I don't understand.")