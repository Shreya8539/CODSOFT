def chatbot():
    print("Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to exit.\n")
    
    while True:
        user_input = input("You: ").lower()
        
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! How can I help you today?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm doing great! How about you?")
        
        elif "your name" in user_input:
            print("Chatbot: I'm RuleBot, your simple chatbot friend.")
        
        elif "what can you do" in user_input:
            print("Chatbot: I can answer simple questions based on predefined rules.")
        
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you rephrase?")

# Run the chatbot
chatbot()