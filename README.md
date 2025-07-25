
# 🤖 Jarvis – Your Voice-Activated AI Assistant
<p align="center">
**Jarvis is your personal voice-based assistant designed to automate your desktop tasks, chat with intelligence, and respond like your desi tech-savvy buddy.**
</p>

<p align="center">
  <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExejR3azlzZjhzNXF1MWdiOTltbG9mNTM0N2w2enJya2Z2NWhkM25rMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/aWclbRb938Tc8FFAvH/giphy.gif" />
</p>


---

## 🚀 Features

- 🎙️ **Wake-Word Activation**  
Say “wake up Jarvis” and start talking.

- 💬 **Natural Conversations**  
Hinglish voice input gets translated to English and answered smartly.

- ⚡ **Smart Replies**  
Powered by LLaMA 3.3 via Groq API — casual, witty, and helpful.

- 📁 **Task Automation**  
Open/close apps, access files, take screenshots, and run calculations.

- 🖥️ **Web Search**  
Ask anything and it will Google it for you.

- 🎵 **Entertainment**  
Play songs/videos via YouTube directly by voice.

- 📰 **Latest News**  
Get top headlines from India with one command (NewsAPI).

- 🔋 **System Monitoring**  
Battery level and internet speed checks via voice.

- 🤗 **Mood Interaction**  
Understands how you're feeling and reacts accordingly.

<p align="center">
  <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXoyeG9sZ202bm13ZHd1bDhyczI5N2ZuajFmbDlzN2NtNmczcWYxMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/zWanaljSNTDvs4hpgg/giphy.gif" width='200'/>
</p>

---

## 🧰 Tech Stack

### 🧠 Backend (Python)
- `speech_recognition` – Voice input  
- `pyttsx3` – Text-to-speech  
- `groq`, `deep_translator` – LLM + Hinglish processing  
- `AppOpener`, `os`, `pyautogui` – Automation  
- `psutil`, `speedtest`, `webbrowser`, `requests` – System/API tasks  

### 🌐 Frontend (Planned)
- `HTML + CSS` – Web UI structure  
- `JavaScript` – Event interaction  
- `Web Speech API` – Microphone input via browser  
- `Fetch API` – Communicates with backend  

### 🔁 Communication
- **FastAPI** – Backend-server bridge for frontend integration

### ☁️ Deployment
- **Frontend Hosting**: Netlify  
- **Backend Hosting**: Render / Replit  

---

## 📂 Project Structure
```
├── ai.py                  # Main logic file
├── src/
│   ├── jarvis intro.mp3   # Voice response files
│   └── jarivs wish.mp3
├── .env                   # API keys (keep secret)
├── requirements.txt       # Python dependencies
├── README.md              # This file
```

---

## 🧪 How to Run
```bash
# Install dependencies
pip install -r requirements.txt

# Setup your .env file
GROQ_API_KEY=your_groq_key
NEWS_API_KEY=your_newsapi_key

# Launch Jarvis
python ai.py
```

> 🎧 Tip: Use a wired headset or configure `device_index` correctly in `take_command()` for better results.

---

## 👨‍💻 Contributor

- [**Ashish Sharma** (AI-ash)](https://github.com/AI-ash)

<p align="right">
  <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGgycjg5bHk0end0b2Z2YWMzcTYza295Nzk3Mm50cXJmN2lpM2hmaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/4rdh8gpiqiDm0/giphy.gif" width="200" />
</p>
