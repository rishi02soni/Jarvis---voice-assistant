# 🤖 Jarvis AI Voice Assistant

A modular, scalable **Python-based Voice Assistant (Jarvis)** that can perform tasks like web search, system control, media playback, and information retrieval using voice commands.

---

## 🚀 Features

* 🎤 Voice Recognition (Speech-to-Text)
* 🔊 Text-to-Speech Response
* 🌐 Open Websites (Google, YouTube, etc.)
* 🔍 Google Search Automation
* 📚 Wikipedia Search
* ⏰ Time & Date Information
* 💻 Open System Applications (VS Code, Chrome, Notepad)
* 🎵 Play YouTube Music
* 🧠 Modular & Clean Code Architecture

---

## 🏗️ Project Structure

```
jarvis-ai/
│── main.py
│── config.py
│
├── core/
│   ├── voice_engine.py
│   ├── command_engine.py
│
├── features/
│   ├── web.py
│   ├── system.py
│   ├── media.py
│   ├── info.py
│
├── utils/
│   ├── helpers.py
│
└── requirements.txt
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/jarvis-ai.git
cd jarvis-ai
```

### 2️⃣ Create Virtual Environment (Recommended)

```
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ⚠️ PyAudio Installation Fix (Important)

If you face issues installing PyAudio:

```
pip install pipwin
pipwin install pyaudio
```

---

## ▶️ Usage

Run the assistant:

```
python main.py
```

---

## 🧠 How It Works

1. `voice_engine.py` → Handles speech recognition & TTS
2. `command_engine.py` → Processes commands
3. `features/` → Contains all functionalities
4. `main.py` → Entry point of the application

---

## 🗣️ Supported Commands

* "Open Google"
* "Open YouTube"
* "Search Python tutorials"
* "Play Arijit Singh songs"
* "Tell me the time"
* "Tell me the date"
* "Open VS Code"
* "Wikipedia Elon Musk"
* "Stop" / "Exit"

---

## 🛠️ Tech Stack

* Python 3.x
* SpeechRecognition
* Pyttsx3
* PyWhatKit
* Wikipedia API
* OS & Webbrowser modules

---

## 📌 Future Enhancements

* 🤖 AI Integration (LLMs / ChatGPT)
* 🧠 Memory System (Database)
* 🖥️ GUI Interface (Tkinter / Electron / React)
* 🔐 Face Recognition Login
* 📱 Mobile App Integration
* 🗂️ Task Automation & Scheduling

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Make changes
4. Submit a PR

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Rishi Soni**
Aspiring Software Engineer | AI & Cloud Enthusiast

* GitHub: https://github.com/rishi02soni

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
