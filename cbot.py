import pyttsx3
import re
import unicodedata
import random
import pyjokes
import time

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def clean_text(text):
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

intents = {
    "greeting": ["hi", "hello", "hey", "hola", "bonjour", "ciao"],
    "attendance": ["attendance", "present", "absent", "mark attendance", "proxy for attendance"],
    "fees": ["fees", "payment", "fee"],
    "joke": ["joke", "tell me a joke", "make me laugh", "funny"],
    "bye": ["bye", "goodbye", "exit"]
}

responses = {
    "greeting": ["Hello! How can I help you?", "Hi there! What can I do for you?"],
    "attendance": ["Attendance is marked automatically."],
    "fees": ["Please contact the accounts department."],
    "bye": ["Good day 😊"]
}

def chatbot_response(user_input):
    user_input = clean_text(user_input)
    for intent, keywords in intents.items():
        for kw in keywords:
            if clean_text(kw) in user_input:
                if intent == "joke":
                    return pyjokes.get_joke()
                return random.choice(responses[intent])
    return "Sorry, I didn't understand."

print("Chatbot is running...")
speak("Chatbot is running. How may I help you?")

while True:
    user_input = input("You: ")

    if clean_text(user_input) in ["bye", "exit"]:
        reply = "Good day"
        print("Chatbot:", reply)
        speak(reply)
        time.sleep(0.5)  # 🔹 crucial: wait for audio
        break

    reply = chatbot_response(user_input)
    print("Chatbot:", reply)
    speak(reply)
