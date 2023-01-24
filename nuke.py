
from time import strftime
from turtle import st
import webbrowser # web link
import pyttsx3  # voice module
import speech_recognition as sr  # VOICE MODULE
import wikipedia
import psutil
import datetime
import os  # for songs and apps
import random
import pyjokes
import pyautogui

command = pyttsx3.init()
#command.say('welcome')    #  .say is output
#command.runAndWait()    #will execute the command

command.setProperty('rate', 170)     # setting voice pace/rate~
voices = command.getProperty('voices')
command.setProperty('voice',voices[1].id)     # changes the male0 voice to

def run(audio):
    command.say(audio)
    command.runAndWait()

def intro():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        run('good morning')
    elif hour>=12 and hour <18:
        run('good afternoon')
    else:
        run('good evening')
        time()
        date()
        run('i am nuke , how may i help you')

def time():
    time = datetime.datetime.now().strftime('%H:%M:%S')
    run('the current time is')
    run(time)


def date():
    year= datetime.datetime.now().year
    month= datetime.datetime.now().month
    date=datetime.datetime.now().date()
    run('today is')
    run(date)
    run(month)
    run(year)

def take_command():

    r =sr.Recognizer()
    with sr.Microphone() as source:
        print('listening.........')
        r.pause_threshold = 1  #         will provied 1 sec time
        audio = r.listen(source)

    try:
        print('recognizing.....')
        query = r.recognize_google(audio,language='en-in')
        print(f'the command is {query}')

    except Exception as e:
        print("please say that again")
        return 'NONE'
    return query


if __name__=="__main__" :
    intro()
    take_command()
    if 1:
        query = take_command().lower()
        if 'wikipedia' in query:
            run('seraching in wikipedia..')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences = 2)   # sentences not working
            run('according to wikipedia')
            print(results)
            run(results)
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'anime' in query:
            webbrowser.open('gogoanime.pe')      

        elif 'netflix' in query:
            webbrowser.open('netflix.com')

        elif 'open code' in query:
            source ="F:\Microsoft VS Code\Code.exe"
            os.startfile(source)

        elif 'open dreamweaver' in query:
            source = "C:\Program Files\Adobe\Adobe Dreamweaver 2021\Dreamweaver.exe"
            os.startfile(source)

        elif 'open photoshop' in query:
            source = "C:\Program Files\Adobe\Adobe Photoshop 2021\photoshop.exe"
            os.startfile(source)

        elif 'open pdf' in query:
            source ="C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"
            os.startfile(source)    

        elif 'play music' in query:
            folder = 'F:\python songs'
            songs =os.listdir(folder)  # listing of songs
            print(len(songs))
            size = len(songs)-1
            n = random.randint(0,size)
            print(n)       
            os.startfile(os.path.join(folder,songs[n])) # songs play

        elif 'cpu status' in query:
            usage = str(psutil.cpu_percent())
            run(f'cpu is at {usage}')
            batery = psutil.sensors_battery()
            run(f'cpu battery is {batery}')

        elif 'joke' in query:
            run(pyjokes.get_jokes())

        elif ' rest' in query:
            run('bye sir ! have a good day')
            quit()    

        elif 'take a note' in query:
            run('taking note sir!!')
            notes = take_command()
            file = open('notes.txt','w')
            run('should i include date and time')
            ans = take_command()
            if 'yes' in ans:
                strTime =datetime.datetime.now().strftime('%H:%H:%S')
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                run('ok doki completed!!')
            else:
                file.write(notes)
        elif 'show notes' in query:
            run('showing notes')
            file = open('notes.txt','r')
            print(file.read())
            run(file.read())

        elif 'screenshot' in query:
            img= pyautogui.screenshot()
            img.save('C:/Users/Dell/Pictures/ss.png')