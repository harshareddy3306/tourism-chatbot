def chatbot():
    print("Tourism Bot: Ask me about tourist places (type 'exit' to quit).")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Tourism Bot: Have a great trip!")
            break
        elif "beach" in user_input:
            print("Tourism Bot: Goa and Vizag are popular beach destinations.")
        elif "temple" in user_input:
            print("Tourism Bot: Tirupati and Madurai are famous temple cities.")
        elif "hill" in user_input:
            print("Tourism Bot: Ooty and Manali are beautiful hill stations.")
        else:
            print("Tourism Bot: Sorry, I couldn't understand that.")

chatbot()
