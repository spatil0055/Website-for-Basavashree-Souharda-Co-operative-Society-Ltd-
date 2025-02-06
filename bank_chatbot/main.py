from chatbot import chatbot_response

print("Welcome to XYZ Bank Chatbot! Type 'exit' to end the chat.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye! Have a great day.")
        break
    print("Bot:", chatbot_response(user_input))

