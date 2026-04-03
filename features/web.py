import webbrowser
from core.voice_engine import speak

def open_website(url):
    speak("Opening website")
    webbrowser.open(url)

def google_search(query):
    speak("Searching on Google")
    webbrowser.open(f"https://www.google.com/search?q={query}")
