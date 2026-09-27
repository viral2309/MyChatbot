print("🤖 My Chatbot")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How are you?")

    elif user == "how are you":
        print("Bot: I am fine! 😊")

    elif user == "what is your name":
        print("Bot: My name is viral 🤖")

    elif user == "bye":
        print("Bot: Goodbye! 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
        print("🤖 Welcome to MyChatbot!")
print("Type 'bye' to exit.")

name = input("Bot: What is your name? ")
print("Bot: Nice to meet you, " + name + "! 😊")

while True:
    user = input(name + ": ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello " + name + "! 👋")

    elif user == "how are you":
        print("Bot: I am fine! How are you? 😊")

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

                elif user == "joke":
        print("Bot: Why do programmers prefer dark mode?")
        print("Bot: Because light attracts bugs! 😂")

    elif user == "date":
        from datetime import datetime
        today = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", today)

    elif user == "time":
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M:%S %p")
        print("Bot: Current time is", current_time)

    elif user == "help":
        print("Bot: You can ask me:")
        print("- hello")
        print("- how are you")
        print("- what is your name")
        print("- who made you")
        print("- calculator")
        print("- joke")
        print("- date")
        print("- time")
        print("- bye")

    elif user == "what is your name":
        print("Bot: My name is viral 🤖")

    elif user == "who made you":
        print("Bot: I was created using Python!")

    elif user == "bye":
        print("Bot: Goodbye " + name + "! See you soon 👋")
        break

    else:
        print("Bot: I'm sorry, I don't understand that. Can you try something else? 🤔")~