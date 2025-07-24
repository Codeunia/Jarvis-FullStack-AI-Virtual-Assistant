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
from audioplayer import AudioPlayer
from dotenv import load_dotenv
from groq import Groq
from deep_translator import GoogleTranslator
load_dotenv()

def speak(audio):
    try:
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 160)
        print(audio)
        engine.say(audio)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(f"[Audio Error] {e}")

def take_command():
    r = sr.Recognizer()
    try:
        with sr.Microphone(device_index=1) as source:  # change index to your microphone check which suits you better
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=7, phrase_time_limit=10)

        print("Recognizing...")
        spoken_text = r.recognize_google(audio, language='hi-IN')  # Mixed Hindi + English

        translated = GoogleTranslator(source='auto', target='en').translate(spoken_text)

        if translated.lower() != spoken_text.lower():
            return translated.lower()
        else:
            return spoken_text.lower()

    except sr.WaitTimeoutError:
        print("Listening timed out.")
    except sr.UnknownValueError:
        print("Speech not understood.")
    except sr.RequestError:
        print("API request failed.")
    except Exception as e:
        print(f"[Take Command Error] {e}")
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
        speak(f"Good Morning Sir. It's {currenttime}")
    elif hour < 18:
        speak(f"Good afternoon Sir. It's {currenttime}")
    else:
        speak(f"Good evening Sir. It's {currenttime}")

    speak("I am ready to work sir.")

def ai_talk(prompt):
    client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),)
    prompt = prompt.replace("jarvis","")

    chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system",
            "content": "You are a smart personal assistant but an Indian desi boy and your name is jarvis that provides answer to the user questions in efficient way not too long somwhere between 2-3 summary. and answer a question in human way",},
        {
            "role": "user",
            "content": f"{prompt}",
        }
    ],
    model="llama-3.3-70b-versatile",
    temperature=2,
)
    speak(chat_completion.choices[0].message.content)
            
def news():
    speak("Fetching the latest news.")
    try:
        NEWS_API_KEY = os.getenv("NEWS_API_KEY")
        main_url = f"https://newsapi.org/v2/everything?q=India&from={date.today() - timedelta(days= 1 )}&sortBy=publishedAt&language=en&pageSize=5&apiKey={NEWS_API_KEY}"
        main_page = requests.get(main_url).json()
        articles = main_page.get("articles")
        head = []
        day = ["first", "second", "third", "fourth", "fifth"]
        if not articles:
            print("No articles found!")
        else:
            for ar in articles[:5]:  # Only take up to 5 art
                head.append(ar.get("title", "No Title"))
        speak("Here some latest news: ")
        for i in range(len(head)):
            speak(f"{head[i]}")
    except Exception as e:
        speak("Unable to fetch news at the moment.")
        print(f"[News Error] {e}")

def battery():
    try:
        battery = psutil.sensors_battery()
        percentage = battery.percent
        speak(f"Sir, our system has {percentage} percent battery.")
        if percentage >=99:
            speak('We are overflowing with power sir')
        elif percentage >= 75:
            speak("We have enough power to continue our work.")
        elif 40 <= percentage < 75:
            speak("We should connect our system to charging.")
        elif 15 <= percentage < 40:
            speak("We don't have enough power to work. Please connect to charger.")
        else:
            speak("Very low power. Connect to charger or the system will shut down soon.")
    except Exception as e:
        print(f"[Battery Error] {e}")
        speak("Unable to fetch battery details.")

def i_speed():
    try:
        st = speedtest.Speedtest()
        dl = st.download()
        up = st.upload()
        speak(f"Download speed is {dl/1024/1024:.2f} Mbps. Upload speed is {up/1024/1024:.2f} Mbps.")
    except Exception as e:
        speak("Unable to check internet speed.")
        print(f"[Speed Error] {e}")

def google_search():
    speak("What should I search on Google?")
    cm = take_command().lower()
    webbrowser.open(f"https://www.google.com/search?q={cm}")

def open_command(query):
    query = query.replace("jarvis open", "")
    speak(f"Opening {query}")
    AppOpener.open(query, output=False, match_closest=True)

def close_command(query):
    query = query.replace("jarvis close", "")
    speak(f"Closing {query}")
    AppOpener.close(query, output=False, match_closest=True)

def calculate():
    speak('Please type what you want to calculate')
    try:
        expression = input("Enter expression: ")
        result = eval(expression)
        speak(f"The answer is {result}")
    except:
        speak("Sorry, I couldn't calculate that.")

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
    img = pyautogui.screnshot()
    img.save(f"{name}.png")
    speak("Screenshot saved.")


def taskExecution():
    wish()
    while True:
        try:
            query = take_command()
            if query == "none":
                continue
                
            elif "jarvis" in query:   
                pass
                if "open google" in query:
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

                elif "calculate" in query or "open calculator" in query:
                    calculate()

                elif 'play song' in query or 'play video' in query:
                    play()

                elif "how are you" in query:
                    hru(query=query.replace("jarvis",''))

                elif "news" in query:
                    news()

                elif "take screenshot" in query:
                    ts()

                elif "shutdown" in query or "you can sleep" in query or "goodbye" in query:
                    speak("Goodbye for righ now sir.")
                    break

                else:
                    try:
                        ai_talk(query)
                    except Exception as e:
                        speak("Sorry sir, I couldn’t process the query. Because of ",e)
            
        except Exception as e:
            print(f"[Loop Error] {e}")
            speak("Some bugs just hit me, but don't worry sir I am still running.")

if __name__ == "__main__":
    taskExecution()
