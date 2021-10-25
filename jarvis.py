import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui
import psutil #pip install psutil
#import pyjokes #pip install pyjokes

from wikipedia.wikipedia import search

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

newVoiceRate = 180
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The time right now is")
    speak(time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Today's date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome to Laptop")
    hour = datetime.datetime.now().hour

    if hour >=6 and hour <=12:
        speak("Good Morning Sir")
    elif hour >12 and hour <=16:
        speak("Good Afternoon Sir")
    elif hour >16 and hour <21:
        speak("Good Evening Sir")
    else:
        speak("Good to See you Sir")
    
    speak("I am JARVIS, the AI Assisstant of this Laptop. How may i help you ?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en=in')
        print(query)
    except Exception as e:
        print(e)
        speak("say that again please")

        return "None"

    return query


def sendmail(to,content):
    server = smtplib.SMTO("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("","")
    server.sendmail("", to, content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save("")


def cpu():
    usage = str(psutil.cpu_percent())
    speak("Cpu is at "+usage)

    battery = psutil.sensors_battery()
    speak("Battery is at ")
    speak(battery.percent)


#def jokes():
#    speak(pyjokes.get_joke())

if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            speak("Bye and Have a great Day Sir, JARVIS now going offline")
            quit()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        elif "send email" in query:
            try:
                speak("What to send ?")
                content = takeCommand()
                to = ""
                #sendmail(to,content)
                speak(content)
                speak("The mail was sent successfully")
            except Exception as e:
                speak(e)
                speak("The mail was not sent")

        elif "open in chrome" in query:
            speak("What do I search ?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        
        #elif "logout" or "log out" in query:
            #os.system("shutdown -l")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "play songs" in query:
            songs_dir = "D:\Songs"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif "remember that" in query:
            speak("What should i remember?")
            data = takeCommand()
            speak("You said me to remember,"+data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()

        #elif "do you remember" or "do you remember anything" in query:
            #remember = open("data.txt","r")
            #speak("you told me to remember that" + remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("Your screenshot has been taken.")

        elif "cpu" in query :
            cpu()

        elif "joke" in query:
            speak("Why did The Joker have to sleep with his lights on? Because he was afraid of the Dark Knight.")
