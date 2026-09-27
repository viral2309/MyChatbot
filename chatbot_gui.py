import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime


def send_message(event=None):
    user_message = entry.get().strip()

    if user_message == "":
        return

    chat_box.insert(tk.END, "You: " + user_message + "\n", "user")

    message = user_message.lower()

    if message in ["hello", "hi", "hey"]:
        response = "Hello! 👋 How can I help you?"

    elif message == "how are you":
        response = "I am fine! 😊 Thanks for asking."

    elif message == "what is your name":
        response = "My name is viral 🤖"

    elif message == "who made you":
        response = "I was created using Python."

    elif message == "joke":
        response = "Why do programmers prefer dark mode?\nBecause light attracts bugs! 😂"

    elif message == "date":
        response = "Today's date is " + datetime.now().strftime("%d-%m-%Y")

    elif message == "time":
        response = "Current time is " + datetime.now().strftime("%I:%M:%S %p")

    elif message == "help":
        response = "Try: hello, how are you, joke, date, time, or bye."

    elif message == "bye":
        response = "Goodbye! 👋 See you again!"

    else:
        response = "Sorry, I don't understand that yet. Type 'help' to see what I can do."

    chat_box.insert(tk.END, "Bot: " + response + "\n\n", "bot")
    chat_box.see(tk.END)

    entry.delete(0, tk.END)


def clear_chat():
    chat_box.delete("1.0", tk.END)
    chat_box.insert(tk.END, "Bot: Chat cleared! 👋\n\n", "bot")


# Main window
window = tk.Tk()
window.title("MyChatbot 🤖")
window.geometry("600x700")
window.resizable(False, False)

# Header
header = tk.Label(
    window,
    text="🤖 MyChatbot",
    font=("Arial", 24, "bold")
)
header.pack(pady=15)

subtitle = tk.Label(
    window,
    text="Your simple Python virtual assistant",
    font=("Arial", 11)
)
subtitle.pack()

# Chat box
chat_box = scrolledtext.ScrolledText(
    window,
    width=65,
    height=28,
    font=("Arial", 11),
    wrap=tk.WORD
)
chat_box.pack(padx=15, pady=15)

# Text formatting
chat_box.tag_config("user", font=("Arial", 11, "bold"))
chat_box.tag_config("bot", font=("Arial", 11))

# Welcome message
chat_box.insert(
    tk.END,
    "Bot: Welcome to MyChatbot! 🤖\n"
    "Bot: Type 'help' to see available commands.\n\n",
    "bot"
)

# Bottom frame
bottom_frame = tk.Frame(window)
bottom_frame.pack(pady=5)

# Input
entry = tk.Entry(
    bottom_frame,
    width=42,
    font=("Arial", 13)
)
entry.pack(side=tk.LEFT, padx=5)

# Send button
send_button = tk.Button(
    bottom_frame,
    text="Send",
    font=("Arial", 11, "bold"),
    command=send_message
)
send_button.pack(side=tk.LEFT, padx=5)

# Clear button
clear_button = tk.Button(
    bottom_frame,
    text="Clear",
    font=("Arial", 11, "bold"),
    command=clear_chat
)
clear_button.pack(side=tk.LEFT, padx=5)

# Press Enter to send
entry.bind("<Return>", send_message)

# Start application
window.mainloop()