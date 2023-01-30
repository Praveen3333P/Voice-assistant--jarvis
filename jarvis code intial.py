#from http import server
#import smtplib ----> used for sending mail 
import webbrowser
from numpy import take
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import pyjokes

print("Initializing")
MASTER = "Praveen"
engine= pyttsx3.init('sapi5')   #-----> sapi5 is microsoft speech API
voices = engine.getProperty('voices')   #inbuilt microsoft gives two different voices 0-boy  1-girl
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() #makes the speech audible in system


def wishMe():
    hour =  int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!" + MASTER)

    elif hour>12 and hour<18:
        speak ("Good Afternoon" + MASTER)

    else :
        speak("Good Evening" + MASTER)  

    speak("I am Jarvis Sir,Please tell me how can I help you") 

def takeCommand():  #---->takes microphone input from user and return string output
    r = sr.Recognizer()  #--->helps to detect the the audio
    with sr.Microphone() as source: #--->for taking the input
        print("Listening.....")
        r.pause_threshold = 1  #seconds of non speaking audio before a phrase is considered complete 
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        print('can you please say that again!!!!!!')
        return "None"
    return query    

#def sendEmail(to, content): ----> for sending mail 
#server =smtplib.SMTP('smtp.gmail.com', 587)
#server.ehlo()
#server.starttls()
#server.login('praveen301102@gmail.com','************')
#server.sendmail('praveen301102@gmail.com',to,content)
#server.close()

#I have commented this because for this we have use the mail id and 
#we have give access to less secure apps in gmail
#which will be an privacy issue for some people.


        
if __name__ == "__main__":     #main method starts from here
   speak('Initializing')
   wishMe()
   while True:
        query = takeCommand().lower() #----> helps in converting into lower case letter
    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query = query.replace('wikipedia'," ")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("www.google.com")    
        elif 'open github' in query:
            webbrowser.open("www.github.com")
        elif 'open webtoon' in query:
            webbrowser.open("www.webtoon.com") 
        elif 'play songs ' in query:
            webbrowser.open("www.spotify.com") 
        elif 'play music'  in query:
            music_dir = 'C:\\Users\\Public\\Downloads\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'tell me a joke' in query:
            random_joke = pyjokes.get_joke()    #----> used pyjokes modules for getting jokes
            print(random_joke)
            speak(random_joke)    
        elif 'the time ' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        #elif 'email to Praveen' in query:
          #  try:
              #  speak("What should I say")
               # content = takeCommand()
               # to = "praveen301102@gmail.com"
               # sendEmail(to,content)
               # speak("Email has been sent")
           # except Exception as e:
               # print(e)
               # speak("Sorry sir,I am unable to send this email") 
        elif 'quit' in query:
            speak("Thank You for using Jarvis. Have a great day")
            exit()
        
            
