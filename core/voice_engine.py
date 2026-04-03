import pyttsx3
import speech_recognition as sr
from config import VOICE_RATE

engine = pyttsx3.init()
engine.setProperty('rate', VOICE_RATE)

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"You: {command}")
        return command.lower()
    except:
        return "none"
