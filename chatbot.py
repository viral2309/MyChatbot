print("🤖 My Chatbot")
print("Type 'bye' to exit.")

name = input("Bot: What is your name? ")
print("Bot: Nice to meet you, " + name + "! 😊")

while True:
    user = input(name + ": ").lower()

    if user in ("hello", "hi"):
        print("Bot: Hello " + name + "! 👋")

    elif user == "how are you":
        print("Bot: I am fine! How are you? 😊")

    elif user == "what is your name":
        print("Bot: My name is MyChatbot 🤖")

    elif user == "who made you":
        print("Bot: I was created using Python!")

    elif user in ("help", "what can you do"):
        print("Bot: I can say hello, answer simple questions, do basic math, tell jokes, and say goodbye. 🤖")
        print("Bot: You can also ask me: calculator, joke, date, time, weather, bye")

    elif user in ("joke", "tell me a joke", "funny"):
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs! 😄")

    elif user in ("weather", "how is the weather"):
        print("Bot: I can't check live weather, but I can tell you it's a great day to smile and be productive! ☀️")

    elif user == "calculator":
        print("Bot: Sure! Let's calculate 🧮")
        num1 = float(input("Bot: Enter first number: "))
        operator = input("Bot: Enter operator (+, -, *, /): ")
        num2 = float(input("Bot: Enter second number: "))

        if operator == "+":
            print("Bot: Answer =", num1 + num2)
        elif operator == "-":
            print("Bot: Answer =", num1 - num2)
        elif operator == "*":
            print("Bot: Answer =", num1 * num2)
        elif operator == "/":
            if num2 != 0:
                print("Bot: Answer =", num1 / num2)
            else:
                print("Bot: Cannot divide by zero.")
        else:
            print("Bot: Invalid operator.")

    elif user == "date":
        from datetime import datetime
        today = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", today)

    elif user == "time":
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M:%S %p")
        print("Bot: Current time is", current_time)

    elif user in ("bye", "goodbye"):
        print("Bot: Goodbye " + name + "! See you soon 👋")
        break

    else:
        print("Bot: I'm sorry, I don't understand that. Can you try something else? 🤔")