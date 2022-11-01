import webbrowser  #Module use for access web application
import pyttsx3     #Module use to convert text into speech
import datetime    #Module use for date and time
import speech_recognition as sr    #Module use for recognizing speech
import wikipedia     #Module use for acess wikipedia
import os            #Module use for access os application

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# engine.setProperty(voice,voice[0].id)
def speak(audio):    #It is a speak function that speak text
    engine.say(audio)
    engine.runAndWait()
def wishme():
    time = int(datetime.datetime.now().hour)
    if (time>12) and (time<20):
        speak("Good Afternoon Sir")
    elif (time>20) and (time<24):
        speak("Good Night Sir")
    else:
        speak("Good Morning")
    speak("How may I hep you Sir")

def takeCommand():    #This function is for taking command

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listerning") 
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio)
        print("User said ",query)
    except Exception as e:
        query="Say that again sir"
        return "None"
    return query

wishme()
query=takeCommand().lower()
speak(query)
if 'wikipedia' in query:
    speak('Searching wikipedia....')
    query = query.replace('wikipedia',"")
    result=wikipedia.summary(query,sentences=1)
    speak('According to wikipedia')
    speak(result)
elif "youtube" in query:
    webbrowser.open("youtube.com")
elif "google" in query:
    webbrowser.open("google.com")
elif "notepad" in query:
    notepad="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories"
    os.startfile(notepad)
