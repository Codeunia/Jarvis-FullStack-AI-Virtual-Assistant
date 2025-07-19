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
import sys
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

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id) #you can change the voices with chnging it's index
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# def take_command():
#     r = sr.Recognizer()
#     with sr.Microphone(device_index=0) as source:
#         print("listenting....")
#         r.pause_threshold = 1
#         audio = r.listen(source,timeout=3,phrase_time_limit=5)

#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         #print(f"User said: {query}")

#     except Exception :
#         #speak("Say that again please...")
#         return "none"
#     query = query.lower()
#     return query

def take_command():
    r = sr.Recognizer()
    with sr.Microphone(device_index=11) as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)  # Helps reduce false triggers
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return "none"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        print(f"Recognition error: {e}")
        return "none"

    return query.lower()


def wish():
    AudioPlayer("C:/Users/shivam/Desktop/Projects/Jarvis/src/jarivs wish.mp3").play(block=True)
    hour = int(datetime.datetime.now().hour)
    t = time.localtime()
    currenttime = time.strftime("%H:%M %p", t)
    

    if hour>=0 and hour<12:
        speak(f"Good Morning Sir. It's {currenttime}") 
    elif hour>=12 and hour<=18:
        speak(f"Good afternoon Sir. It's {currenttime}")
    else:
        speak(f"Good evening Sir. It's {currenttime}") 
    
    speak("I am ready to work sir." )   

def news():
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    main_url = f'http://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day=["first","second","third","fourth","fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"Today's {day[i]} news is: {head[i]}")

def battery():
      battery = psutil.sensors_battery()
      percentage = battery.percent
      speak(f"Sir, our system have {percentage} parcent battery.")
      if percentage>=75:
          speak('We have enough power to continue our work.')
      elif percentage>=40 and percentage<=75:
          speak("We should connect our system to charging point to charge our battery.")
      elif percentage>=15 and percentage<=40:
          speak("We don't have enough power to work, pleae connect to charger.")
      elif percentage<=15:
          speak("We have very low power, please connect to charger otherwise system will shutdown very soon.")

def i_speed():
    st = speedtest.Speedtest()
    dl = st.download()
    up = st.upload()
    speak(f"Sir our downloading speed is {dl} bit per second and uploading speed is {up} bit per second.")
             
def taskExecution():
     wish ()
     while True:
         
    #  if 1:

          query = take_command().lower()

          
        
          if "open"in query:
              if 'jarvis' in query:
                query=query.replace("jarvis open",'')
                
              else:
                query=query.replace("open",'')
              speak(f'Opening {query}')
              AppOpener.open(f'{query}',output=False,match_closest=True)
          
          elif "close" in query:
              if 'jarvis' in query:
                query=query.replace("jarvis close",'')
                
              else:
                query=query.replace("close",'')
              speak(f'Closing {query}')
              AppOpener.close(f'{query}',output=False,match_closest=True)

          elif "how much power left" in query or "how much power we have" in query or "battery" in query:
              battery()

          if "introduce yourself" in query:
              AudioPlayer("C://Users//shivam//Desktop//Projects//Jarvis//src//jarvis intro.mp3").play(block=True)
                
          if "internet speed" in query:
              i_speed()

          elif 'wikipedia' in query or 'who is' in query:
              speak("Searching wikipedia...")
              query = query.replace("wikipedia","")
              results = wikipedia.summary(query, sentences=2)
              speak("According to wikipedia")
              speak(results)

          if "open youtube" in query:
              webbrowser.open("www.youtube.com")

          elif "answer" in query or "question" in query:
              speak('Sir, please write the question.')
              question = input('QUESTION:')
              max_results = 1
              WOLFRAM_APP_ID = os.getenv("WOLFRAM_APP_ID")
              client = wolframalpha.Client(WOLFRAM_APP_ID)
              res = client.query(question)
              answer = next(res.results).text
              speak(answer)

          elif "calculate" in query or "open calculator" in query:
              speak('Sir, please write what you want to calculate')
              print(eval(input("Enter the expression: ")))

          if "open google" in query:
              speak("sir,what should I search on google")
              cm = take_command().lower()
              webbrowser.open(f"https://www.google.com/search?q={cm}")

          if 'play song on youtube' in query or 'play video on youtube' in query:
              if 'vedio' in query:
                  speak("Sir, which vedio you want to watch")
              else:
               speak("Sir, which song you like to hear")
              gh = take_command().lower()
              pywhatkit.playonyt(f'{gh}')
              speak(f"Ok sir,playing {gh}")

          if "thank you" in query:
              speak("It's my pleasure sir.")

          elif 'joke' in query:
              speak(pyjokes.get_joke())

          elif "you can rest" in query or "you can sleep" in query:
              speak('Ok sir, I am going to rest, you can call anytime. I am always there for you.')
              break

          elif "how are you" in query:
              speak('I am fine sir, what about you. ')
              condition = take_command()
              if "fine" in condition or "good" in condition or "happy" in condition:
                  speak("Good to hear sir.")
              elif "not good" in condition or "not happy" in condition or "sad" in condition or "not fine" in condition:
                  speak("Sir what happend, can I do something for you to change your mood.")
                  reply = take_command()
                  if "music" in reply:
                      speak("Sir, I am playing your favourite song. I wish than you will be happy")
                      gh = ("505","Shinunoga EWa ","YKWIM","IDFC")
                      pm = random.choice(gh)
                      pywhatkit.playonyt(f'{pm}')
                      speak(f"Sir I am playing {pm}.")
                  else: 
                      pass    
                  
          elif "news" in query:
              speak('Please wait sir, feteching the latest news.')
              news()

          elif "how to" in query:
                max_results = 1
                how_to = search_wikihow(query, max_results)
                assert len(how_to) ==1
                speak(how_to[0].summary)

          elif "take screenshot" in query:
               speak("Sir, please tell me the name for this screenshot file.")
               name = input("Enter name for ss here:")
               speak("Please sir hold the screen for few seconds, I am taking screenshot.")
               time.sleep(2)
               img = pyautogui.screenshot()
               img.save(f"{name}.png")
               speak("I am done sir, now what is the next command for me")
          elif "show me the screenshot" in query:
                try:
                    img = Image.open(f'C://Users//shivam//{name}')
                    img.show(img)
                    speak("Here it is sir")
                    time.sleep(2)  
                except IOError:
                    speak("Sorry sir, I am unable to display the screenshot")  

          elif "shutdown" in query:
                speak('Thanks for using me sir, have a good day.')
                sys.exit()

          time.sleep(3)
          regreet = ("Sir, do you have any other work?", "Sir, what is next command for me","Sir, now what I do next","Sir, any other task for me"   )
          op = random.choices(regreet)
          speak(f"{op}")     

if __name__ == "__main__":
    taskExecution()
# ................................................................................................................................................