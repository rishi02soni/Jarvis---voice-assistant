from core.voice_engine import speak, listen
from core.command_engine import execute
import datetime

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis. How can I help you?")

def main():
    wish()
    
    running = True
    while running:
        command = listen()
        if command != "none":
            running = execute(command)

if __name__ == "__main__":
    main()
