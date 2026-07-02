print("===== Rule Based Chatbot =====")
print("Type 'bye' to exit\n")

while True:

    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif "how are you" in user:
        print("Bot: I am fine. Thanks for asking.")

    elif "your name" in user:
        print("Bot: My name is RuleBot.")

    elif "help" in user:
        print("Bot: I can answer simple questions.")

    elif "bye" in user:
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")