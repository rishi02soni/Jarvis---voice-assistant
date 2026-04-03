import pywhatkit
from core.voice_engine import speak

def play_youtube(command):
    song = command.replace("play", "")
    speak("Playing on YouTube")
    pywhatkit.playonyt(song)
