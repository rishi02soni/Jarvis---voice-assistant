import os
from core.voice_engine import speak

def open_vscode():
    speak("Opening VS Code")
    os.system("code")

def open_chrome():
    speak("Opening Chrome")
    os.system("start chrome")

def open_notepad():
    speak("Opening Notepad")
    os.system("notepad")
