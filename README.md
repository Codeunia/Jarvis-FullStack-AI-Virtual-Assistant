# 🤖 Jarvis – Your Voice-Activated AI Assistant  

Jarvis is your personal **voice-based AI assistant** — designed to automate desktop tasks, chat smartly, and respond like your desi tech-savvy buddy.  

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM21qcDQzOWViYWcyNjV6b3d5b3JsaHZrYmN6d3ZwbjFhc21ybGdnaCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/SnhVfcLN6DMdYJADWf/giphy.gif" width="300"/>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white" /></a>
  <a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/FastAPI-⚡-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white" /></a>
  <a href="https://groq.com/"><img src="https://img.shields.io/badge/Groq-LLM_API-orange?style=for-the-badge&logo=openai&logoColor=white" /></a>
</p>

---

## ✨ Features  

- 🎙️ **Wake-Word Activation** – Just say *“wake up Jarvis”* and start talking.  
- 💬 **Natural Conversations** – Hinglish input → Fluent witty English replies.  
- ⚡ **Smart Replies** – Powered by **LLaMA 3.3 (Groq API)**.  
- 📂 **Task Automation** – Open/close apps, take screenshots, access files.  
- 🖥️ **Web Search** – Google anything by voice.  
- 🎵 **Entertainment** – Play YouTube songs/videos.  
- 📰 **News Updates** – Get India’s top 5 headlines via **NewsAPI**.  
- 🔋 **System Monitoring** – Check battery + internet speed instantly.  
- 🤗 **Mood Interaction** – Jarvis reacts to your mood (with jokes/music).  

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcW80eWlobXJ0N3g2aGpleWw3MHFzOHl2cG5leGc5cWU5ZWx4eGRiZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/bGgsc5mWoryfgKBx1u/giphy.gif" width="300"/>
</p>

---

## 🧰 Tech Stack  

**Backend (Python):**  
`FastAPI`, `speech_recognition`, `pyttsx3`, `groq`, `deep_translator`,  
`AppOpener`, `pyautogui`, `psutil`, `speedtest`, `requests`  

**Frontend:**  
`HTML`, `CSS`, `JavaScript`, `Web Speech API`, `Fetch API`  
+ Live logs with **Server-Sent Events (SSE)**  

---

## 📂 Project Structure  

```
├── main/
│   ├── app.py             # FastAPI server entry point
│   └── core.py            # Core Jarvis AI logic (voice + automation)
│
├── src/
│   ├── jarvis intro.mp3   # Startup audio
│   └── jarivs wish.mp3    # Greeting audio
│
├── static/
│   ├── home_style.css     # Home page styles
│   ├── style.css
│   └── script.js          # Frontend JS
│
├── templates/
│   ├── index.html         # Landing page
│   └── home.html          # Jarvis UI page (terminal logs)
│
├── .env                   # API keys (keep secret)
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── .gitignore
```

---

## ⚡ Quick Start (Run Locally)  

```bash
# Clone the repo
git clone https://github.com/Codeunia/Jarvis-FullStack-AI-Virtual-Assistant.git
cd Jarvis-FullStack-AI-Virtual-Assistant

# Install dependencies
pip install -r requirements.txt

# Setup your .env file
GROQ_API_KEY=your_groq_key
NEWS_API_KEY=your_newsapi_key

# Run backend server with uvicorn
uvicorn main.app:app --host 127.0.0.1 --port 8000 --reload
```

👉 Open in browser: `http://127.0.0.1:8000/`  

---

## 🎧 Tips  

- Use a **wired headset** for best results.  
- Update `device_index` in `take_command()` (core.py) if Jarvis isn’t hearing you.  
- Logs stream live in the frontend terminal — no need to check console.  

---

## 🤝 Contribution  

This project is created and maintained by [**Ashish Sharma (AI-ash)**](https://github.com/AI-ash).  
All contributions, feedback, and suggestions are welcome to make Jarvis even smarter 🚀  

---

## 📜 License  

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.  

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/AI-ash">Ashish Sharma</a>
</p>

---

<p align="center">
  ⭐ If you enjoy using Jarvis, don’t forget to star the repo — your support keeps it alive and evolving 🚀  
</p>
