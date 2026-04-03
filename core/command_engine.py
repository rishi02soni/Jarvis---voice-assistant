from core.voice_engine import speak
from features import web, system, media, info

def execute(command):
    
    if "wikipedia" in command:
        info.search_wikipedia(command)

    elif "open youtube" in command:
        web.open_website("https://youtube.com")

    elif "open google" in command:
        web.open_website("https://google.com")

    elif "search" in command:
        web.google_search(command)

    elif "play" in command:
        media.play_youtube(command)

    elif "time" in command:
        info.tell_time()

    elif "date" in command:
        info.tell_date()

    elif "open vscode" in command:
        system.open_vscode()

    elif "open chrome" in command:
        system.open_chrome()

    elif "open notepad" in command:
        system.open_notepad()

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False

    else:
        web.google_search(command)

    return True
