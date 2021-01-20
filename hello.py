import pyttsx3                          #pip install pyttsx3 or python3 -m pip install pyttsx3
import datetime
import speech_recognition as sr         #pip install speechrecognition or python3 -m pip install speechrecognition
import wikipedia                        #pip install wikipedia  or python3 -m pip install wikipedia
import smtplib
import webbrowser as wb
import psutil                           #pip install psutil  or python3 -m pip install psutil
import pyjokes                          #pip install pyjokes or python3 -m pip install pyjokes
import os
import pyautogui                        #pip install pyautogui  or  python3 -m pip install pyautogui
import random
import json
import requests
from urllib.request import urlopen
import wolframalpha                      #python3 -m pip install wolframalpha    or pip install wolframaplha
import pyaudio
import time



engine = pyttsx3.init()
wolframalpha_app_id = 'wolframalpha id goes here'     # https://products.wolframalpha.com/api/
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S")  #for 12 hour clock //\\ for 24 hours change "I" to "H"
    speak("The current time is")
    speak(Time)

#time_()

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak(date)
    speak(month)
    speak(year)

#date_()

def wishme():
    speak("welcome back sir!")
    time_()
    date_()

    #Greetings
    hour = datetime.datetime.now().hour

    if hour >=6 and hour <12:
        speak("Good Morning Sir!")
    elif hour >=12 and hour <18:
        speak("Good Afternoon Sir!")
    elif hour >=18 and hour <24:
        speak("Good Night Sir!")

    speak("Me at your service. Please tell me How can i help u")

# wishme()
def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try :
        print("Recognizing...........")
        query = r.recognize_google(audio,language = 'en-US')
        print(query)

    except Exception as e:
        print(e)
        print("Say That Again Please.......")
        return "None"
    return query
#TakeCommand()

def sendmail(to,contant):
    server =smtplib.SMTP('smtp.gmail.com',587)  #587 is port
    server.ehlo()
    server.starttls()
    #for this function ,you must enable low securrity in your gmail
    #which you are going to use as sender
    server.login('username@gmail.com','password')
    server.sendmail('username@gmail.com',to,content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    print('CPU is at'+usage)
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)
def jokes():
    speak(pyjokes.get_joke())

def screenshot():
    ing = pyautogui.screenshot()
    img.save('C:/Users/parih/Desktop/screenshot.png')     #path where u want to save the image


if __name__ == "__main__":
    
    wishme()
    while True:
        query = TakeCommand().lower()  #All Command Will Be Stored In Lower Case

        if 'time' in query:  #tell us time when asked
            time_()

        elif 'date' in query:  #tell us date when asked
            date_()
        
        elif 'wikipedia' in query:
            speak("searching.........")
            query=query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=3)
            speak('According to wikipedia')
            print(speak)
            speak(result)

        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = TakeCommand()
                #provide receiver email address
                speak('Who is the Receiver?')
                receiver=input("Enter Receiver Email :")
               # receiver = 'receiver_is_me@gmail.com'
                to = receiver
                sendEmail(to,content)
                speak(content)
                speak('Email hass been sent')

            except Exception as e:
                print(e)
                speak('unable to end email')

        elif 'search in crome' in query:
            speak('what should i search?')
            cromepath = 'C:\Program Files\Google\Chrome\Application\crome.exe %s'
            #crome path depends on your crome installed location

            search = TakeCommand().lower()
            wb.get(cromepath).open_new_tab(search+'.com') #only open the website with .com at end


        elif 'search youtube' in query:
            speak('what should i search?')
            search_Term = TakeCommand().lower()
            speak("here we go to youtube")
            wb.open('https://www.youtube.com/results?search_query='+search_Term)

        elif 'search google' in query:
            speak('what should i search?')
            search_Term = TakeCommand().lower()
            speak('searching..........')
            wb.open('https://www.google.com/search?search_query='+search_Term)


        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'go offline' in query:
            speak('going offline sir!')
            quit()

        elif 'word' in query:
            speak('opening ms world.......')
            ms_word = r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'
            os.startfile(ms_word)

        elif 'write a note' in query:
            speak('what should i write ,   sir')
            notes = TakeCommand()
            file = open('note.txt','w')
            speak("sir should i include date and time")
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%h:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak("Done Taking Notes")

            else:
                file.write(notes)
        
        elif 'show notes' in query:
            speak('showing notes')
            file = open('note.txt','r')
            print(file.read())
            speak(file.read())

        elif 'take screenshot' in query:
            screenshot()
            
        elif 'play music' in query:
            songs_dir = ''
            music = os.listdir(songs_dir)
            speak('what song u want to play!')
            speak('select a number.........')
            ans = TakeCommand().lower()
            while('number' not in ans and ans != 'random' and ans != 'you choose'):
                speak('i could not understand you plese try again')
                ans = TakeCommand().lower()
            if 'number' in ans:
                no = int(ans.replace('number',''))
            elif 'random' in ans:
                no = random.randint(1,100)
            #no = int(ans.replace('number',''))

            os.startfile(os.path.join(songs_dir,music[no]))

        elif 'remember that' in query:
            speak("what should i remember?")
            memory = TakeCommand()
            speak("you asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('memory.txt','r')
            speak('you asked me to remember that'+remember.read())

        elif 'where is' in query:
            query = query.replace("where is","")
            location = query
            speake("user asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)

        elif 'news' in query:
            try:
                jsonObj = urlopen("your API KEY here")  #https://newsapi.org/     is website se le lena kar lena                data = json.load(jsonObj)
                i=1
                speak('Here are some top headlines from Entertainment Industry')
                print('=============== TOP HEADLINES ==============='+'\n')
                for item in data:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description'+'\n'])
                    speak(item['title'])
                    i += 1

            except Exception as e:
                    print(str(e))

        elif 'calculate' in query:
            client = wolframalpha.client(wolframalpha_app_id)
            index = query.lower().split().index('calculate')
            query = query.split()[index + 1:]
            res = client.query('',join(query))
            answer =next(res.result).text
            print('The Answer is : ' +answer)
            speak('The Answer is : ' +answer)

        elif 'what is' in query or 'who is' in query:
            #use the same API key
            client = wolframalpha.client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.result).txt)
                speak(next(res.result).txt)
            except StopeIteration:
                print('no result')

        elif'stop listening' in query:
            speak('for how many seconds you want me to stop listening  cammand?')
            ans = int(TakeCommand())
            time.sleep(ans)
            print(ans)

        elif 'log out' in query:
            os.system("shutdown -l")
        
        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")