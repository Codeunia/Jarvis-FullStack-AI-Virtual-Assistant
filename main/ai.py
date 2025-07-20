import pyttsx3
import speech_recognition as sr
import os
import AppOpener
import requests
import random
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import pyautogui
import time
import datetime
from subprocess import call
from urllib.request import Request, urlopen
import wolframalpha
from pywikihow import search_wikihow
from PIL import Image
import psutil
import speedtest
from audioplayer import AudioPlayer
from dotenv import load_dotenv
load_dotenv()

def speak(audio):
    try:
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 180)
        print(audio)
        engine.say(audio)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(f"[Audio Error] {e}")

def take_command():
    r = sr.Recognizer()
    try:
        with sr.Microphone(device_index=1) as source:  # change index to your mic
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        return query.lower()

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

def news():
    try:
        NEWS_API_KEY = os.getenv("NEWS_API_KEY")
        main_url = f"https://newsapi.org/v2/everything?q=India&from={datetime.datetime.now().strftime('%Y-%m-%d')}&sortBy=publishedAt&language=en&pageSize=5&apiKey={NEWS_API_KEY}"
        main_page = requests.get(main_url).json()
        articles = main_page.get("articles")
        head = []
        day = ["first", "second", "third", "fourth", "fifth"]
        if not articles:
            print("No articles found!")
        else:
            for ar in articles[:5]:  # Only take up to 5 art
                head.append(ar.get("title", "No Title"))

        for i in range(len(head)):  # Loop only through available headlines
            speak(f"Today's {day[i]} news is: {head[i]}")
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

def taskExecution():
    wish()
    while True:
        try:
            query = take_command()
            if query == "none":
                continue

            if "open" in query:
                query = query.replace("jarvis open", "").replace("open", "")
                speak(f"Opening {query}")
                AppOpener.open(query, output=False, match_closest=True)

            elif "close" in query:
                query = query.replace("jarvis close", "").replace("close", "")
                speak(f"Closing {query}")
                AppOpener.close(query, output=False, match_closest=True)

            elif "how much power" in query or "battery" in query:
                battery()

            elif "introduce yourself" in query:
                AudioPlayer("src//jarvis intro.mp3").play(block=True)
                
            elif "internet speed" in query:
                i_speed()

            elif 'wikipedia' in query or 'who is' in query:
                try:
                    speak("Searching Wikipedia...")
                    query = query.replace("wikipedia", "").replace("who is", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    speak(results)
                except:
                    speak("Sorry, no such character found on Wikipedia.")

            elif "open youtube" in query:
                webbrowser.open("https://www.youtube.com")

            elif "calculate" in query or "open calculator" in query:
                speak('Please type what you want to calculate')
                try:
                    expression = input("Enter expression: ")
                    result = eval(expression)
                    speak(f"The answer is {result}")
                except:
                    speak("Sorry, I couldn't calculate that.")

            elif "open google" in query:
                speak("What should I search on Google?")
                cm = take_command().lower()
                webbrowser.open(f"https://www.google.com/search?q={cm}")

            elif 'play song' in query or 'play video' in query:
                speak("Which one do you want to play?")
                song = take_command()
                pywhatkit.playonyt(song)
                speak(f"Playing {song} on YouTube")

            elif "thank you" in query:
                speak("It's my pleasure sir.")

            elif 'joke' in query:
                speak(pyjokes.get_joke())
                

            elif "how are you" in query:
                speak("I'm fine sir, what about you?")
                condition = take_command()
                if any(word in condition for word in ["fine", "good", "happy"]):
                    speak("Good to hear that.")
                elif any(word in condition for word in ["not", "sad"]):
                    speak("Can I do something to cheer you up?")
                    reply = take_command()
                    if "music" in reply:
                        song = random.choice(["505", "Shinunoga E-Wa", "YKWIM", "IDFC"]) #update ur choice of songs
                        pywhatkit.playonyt(song)
                        speak(f"Playing {song} to make you feel better.")

            elif "news" in query:
                speak("Fetching the latest news.") #might shows old news
                news()

            elif "how to" in query:
                try:
                    how_to = search_wikihow(query, 1)
                    if how_to:
                        speak(how_to[0].summary)
                    else:
                        speak("No relevant how-to found.")
                except:
                    speak("Sorry, I couldn't search that.")

            elif "take screenshot" in query:
                speak("Please give a filename for the screenshot.")
                name = input("Screenshot name: ")
                time.sleep(2)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("Screenshot saved.")

            elif "show me the screenshot" in query:
                try:
                    img = Image.open(f"{name}.png")
                    img.show()
                except:
                    speak("Couldn't display the screenshot.")

            elif "shutdown" in query or "you can sleep" in query:
                speak("Okay sir, shutting down now.")
                break

            else:
                try:
                    WOLFRAM_APP_ID = os.getenv("WOLFRAM_APP_ID") #mstly dont do anything
                    client = wolframalpha.Client(WOLFRAM_APP_ID)
                    res = client.query(query)
                    answer = next(res.results).text
                    speak(answer)
                except Exception as e:
                    speak("Sorry sir, I couldn’t process the query.")
                    print(f"[Wolfram Error] {e}")

            
        except Exception as e:
            print(f"[Loop Error] {e}")
            speak("An unexpected error occurred, but I am still running.")

if __name__ == "__main__":
    taskExecution()
