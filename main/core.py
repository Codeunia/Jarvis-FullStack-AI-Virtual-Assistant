import pyttsx3
import speech_recognition as sr
import os
import AppOpener
import requests
import random
import webbrowser
import pyautogui
import pywhatkit
import time
import datetime
from datetime import date, timedelta
import psutil
import speedtest
import asyncio
from audioplayer import AudioPlayer
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
log_queue = asyncio.Queue()
conversation_history = []
running = True
last_command = None


def log(msg: str):
    try:
        loop = asyncio.get_running_loop()
        loop.create_task(log_queue.put(msg))   
    except RuntimeError:
        asyncio.run(log_queue.put(msg))

def speak(audio):
    log(f"Jarvis: {audio} \n")
    conversation_history.append(f"Jarvis: {audio}")
    try:
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 160)
        engine.say(audio)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        log(f"[Audio Error] {e}")

def take_command():
    r = sr.Recognizer()
    try:
        with sr.Microphone(device_index=1) as source:  # change index to your microphone check which suits you better
            log("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=7, phrase_time_limit=10)

        log("Recognizing...")
        spoken_text = r.recognize_google(audio, language='en-US')
        log(f"User: {spoken_text}")
        conversation_history.append(f"User: {spoken_text}")
        return spoken_text

    except Exception as e:
        log(f"[Take Command Error] {e}")
    return "none"

def wish():
    try:
        AudioPlayer("src//jarivs wish.mp3").play(block=True)
    except:
        pass

    hour = int(datetime.datetime.now().hour)
    t = time.localtime()
    currenttime = time.strftime("%H:%M %p", t)

    if hour < 12:
        speak(f"Good Morning bro. It's {currenttime}")
    elif hour < 18:
        speak(f"Good afternoon bro. It's {currenttime}")
    else:
        speak(f"Good evening bro. It's {currenttime}")

    speak("I am ready to work bro.")


def ai_talk(prompt):
    client = Groq(api_key=os.getenv("GORQ_API_KEY"))
    prompt = prompt.replace("jarvis", "").strip()
    history = "\n".join(conversation_history)

    chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system",
            "content": "You are Jarvis — a witty, cheeky, and street-smart Indian personal assistant"
            "who speaks only in fluent English with a subtle 'desi boy' vibe. "
            "Normally, you reply in 2-3 sentences, keeping responses crisp, fun, and engaging."
            "You mix helpfulness with light sarcasm or playful trolling when appropriate — for example, joking about being overworked."
            "You never sound robotic; you speak like a smart friend."
            "If the user asks for an explanation, description, detailed answer, or says 'tell me more',"
            "you switch to a longer, well-structured and clear response without losing your personality."
            f"you keep record of our conversation in {history} and answer according to it."
            "No need to return about conservation record or any hprintf just reply to what asked"},
        {
            "role": "user",
            "content":f"{history}\n User: {prompt}",
        }
    ],
    model="llama-3.3-70b-versatile",
    temperature=2,
)
    reply = chat_completion.choices[0].message.content

    speak(reply)
    
            
def news():
    speak("Fetching the latest news.")
    try:
        NEWS_API_KEY = os.getenv("NEWS_API_KEY")
        main_url = f"https://newsapi.org/v2/everything?q=India&from={date.today() - timedelta(days= 1 )}&sortBy=publishedAt&language=en&pageSize=5&apiKey={NEWS_API_KEY}"
        main_page = requests.get(main_url).json()
        articles = main_page.get("articles")
        head = []
        if not articles:
            log("No articles found!")
        else:
            for ar in articles[:5]:  # Only take up to 5 art
                head.append(ar.get("title", "No Title"))
        speak("Here some latest news: ")
        for i in range(len(head)):
            speak(f"{head[i]}")
    except Exception as e:
        speak("Unable to fetch news at the moment.")
        log(f"[News Error] {e}")

def battery():
    try:
        battery = psutil.sensors_battery()
        percentage = battery.percent
        speak(f"bro, our system has {percentage} percent battery.")
        if percentage >=99:
            speak('We are overflowing with power bro')
        elif percentage >= 75:
            speak("We have enough power to continue our work.")
        elif 40 <= percentage < 75:
            speak("We should connect our system to charging.")
        elif 15 <= percentage < 40:
            speak("We don't have enough power to work. Please connect to charger.")
        else:
            speak("Very low power. Connect to charger or the system will shut down soon.")
    except Exception as e:
        log(f"[Battery Error] {e}")
        speak("Unable to fetch battery details.")

def i_speed():
    try:
        st = speedtest.Speedtest()
        dl = st.download()
        up = st.upload()
        speak(f"Download speed is {dl/1024/1024:.2f} Mbps. Upload speed is {up/1024/1024:.2f} Mbps.")
    except Exception as e:
        speak("Unable to check internet speed.")
        log(f"[Speed Error] {e}")

def google_search():
    speak("What should I search on Google?")
    cm = take_command().lower()
    webbrowser.open(f"https://www.google.com/search?q={cm}")

def open_command(query):
    query = query.lower().replace("open", "").strip()
    all_apps = AppOpener.give_appnames()
    matched_app = None
    for app in all_apps:
        if app.lower() in query:
            matched_app = app
            break
    if matched_app:
        speak(f"Opening {matched_app}")
        AppOpener.open(matched_app, output=False, match_closest=True)
    else:
        speak("I couldn't detect the app name, bro. Tell me which one to open.")


def close_command(query):
    query = query.lower().replace("close", "").strip()
    all_apps = AppOpener.give_appnames()
    matched_app = None
    for app in all_apps:
        if app.lower() in query:
            matched_app = app
            break
    if matched_app:
        speak(f"Closing {matched_app}")
        AppOpener.close(matched_app, output=False, match_closest=True)
    else:
        speak("I couldn't detect the app name, bro. Tell me which one to open.")

def play():
    speak("Which one do you want to play?")
    song = take_command()
    pywhatkit.playonyt(song)
    speak(f"Playing {song} on YouTube")

def hru(query):
    ai_talk(query)
    speak(" what about you?")
    condition = take_command()
    if any(word in condition for word in ["fine", "good", "happy"]):
        speak("Good to hear that.")
    elif any(word in condition for word in ["not", "sad"]):
        speak("Can I do something to cheer you up?")
        reply = take_command()
        if "music" in reply:
            song = random.choice(["muskurahat by mitraz", "pag pag", "pehli baar dekha", "anokhi si ladki"]) #update ur choice of songs
            pywhatkit.playonyt(song)
            speak(f"Playing {song} to make you feel better.")

def ts():
    speak("Please give a filename for the screenshot.")
    name = take_command()
    time.sleep(2)
    img = pyautogui.screenshot()
    img.save(f"{name}.png")
    speak("Screenshot saved.")


def taskExecution():
    global last_command, running
    wish()
    while running:
        try:
            query = take_command().lower()
            if query == "none":
                continue

            # Remove "jarvis" trigger word if present
            if "jarvis" in query:
                query = query.replace("jarvis", "").strip()

            # ---------- Command checks ----------
            if "open google" in query or "google search" in query or "google " in query:
                google_search()

            elif "open" in query:
                open_command(query)

            elif "close" in query:
                close_command(query)

            elif "how much power" in query or "battery" in query:
                battery()

            elif "introduce yourself" in query:
                AudioPlayer("src//jarvis intro.mp3").play(block=True)

            elif "internet speed" in query:
                i_speed()

            elif 'play song' in query or 'play video' in query:
                play()

            elif "how are you" in query:
                hru(query=query)

            elif "news" in query:
                news()

            elif "take screenshot" in query:
                ts()

            elif "last command" in query or "echo last" in query or "meta" in query:
                if last_command:
                    ai_talk(f"The user is asking what was their last command. Their last actual command was: {last_command}. Answer naturally.")
                    last_command = query
                else:
                    ai_talk("The user asked about their last command, but no command was given yet.")
                last_command = query

            elif "shutdown" in query or "you can sleep" in query or "goodbye" in query or "turn off" in query:
                speak("Goodbye for now bro, shutting myself down.")
                running = False   
                break

            else:
                # Default to AI response if no command matched
                ai_talk(query)

            # Store the last successful command
            last_command = query

        except Exception as e:
            log(f"[Loop Error] {e}")
            speak("Some bugs just hit me, but don't worry bro I am still running.")

async def get_log_stream():
    while True:
        msg = await log_queue.get()
        yield msg

        
# taskExecution()
