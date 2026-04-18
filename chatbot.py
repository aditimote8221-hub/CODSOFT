import datetime
import random

def get_response(user):
    jokes = [
        "Why did the computer go to school? To improve its byte!",
        "Why was the laptop cold? It forgot to close its Windows!",
        "Why do programmers prefer dark mode? Because light attracts bugs!"
    ]

    # Greetings
    if any(word in user for word in ["hello", "hi", "hey"]):
        return random.choice([
            "Hello! 😊",
            "Hi there!",
            "Hey! How can I help you?"
        ])

    # How are you
    elif "how are you" in user:
        return random.choice([
            "I'm doing great! 😊",
            "All good here! What about you?",
            "I'm fine and ready to help!"
        ])

    # Name
    elif "your name" in user:
        return "I am your smart chatbot 🤖"

    # Time
    elif "time" in user:
        return "Current time is " + datetime.datetime.now().strftime("%H:%M:%S")

    # Date
    elif "date" in user:
        return "Today's date is " + str(datetime.date.today())

    # Day
    elif "day" in user:
        return "Today is " + datetime.datetime.now().strftime("%A")

    # Joke
    elif "joke" in user:
        return random.choice(jokes)

    # Thanks
    elif "thank" in user:
        return random.choice([
            "You're welcome! 😊",
            "No problem!",
            "Glad I could help!"
        ])

    # Help
    elif "help" in user:
        return "You can ask me about time, date, day, jokes, or greetings."

    # Simple Calculator
    elif "calculate" in user:
        try:
            expression = user.replace("calculate", "").strip()
            result = eval(expression)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't calculate that."

    # Motivation
    elif "motivate" in user or "sad" in user:
        return random.choice([
            "Don't give up! You're doing great 💪",
            "Every day is a new opportunity 🌟",
            "Believe in yourself!"
        ])

    # About programming
    elif "python" in user:
        return "Python is a powerful and beginner-friendly programming language."

    elif "study" in user:
        return "Stay consistent and practice daily. You will improve!"

    # Exit
    elif user in ["bye", "exit"]:
        return "exit"

    # Default
    else:
        return random.choice([
            "Hmm, I didn't understand that.",
            "Can you rephrase that?",
            "I'm still learning! Try asking something else 😊"
        ])


def chatbot():
    print("🤖 Smart Chatbot Started (type 'bye' to exit)\n")

    while True:
        user = input("You: ").strip().lower()

        if not user:
            print("Bot: Please say something!")
            continue

        response = get_response(user)

        if response == "exit":
            print("Bot: Goodbye! 👋")
            break

        print("Bot:", response)


chatbot()