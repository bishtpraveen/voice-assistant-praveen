import pyttsx3 #pip install pyttsx3 text-to-speech library it supports 2 voices male female provided by sapi5 for windows
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit as kit # to send watsapp msg


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hey praveen. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587) #smtp server address in google  gmail setting
    server.ehlo()#  # message returened by the server is stored #identify yourself to an ESMTP server using EHLO
    server.starttls()   #to provides encryption #puts the connection to the  SMTP server into TLS mode
    server.login('pkb14111998@gmail.com', 'bisht0744')
    server.sendmail('pkb14111998@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        #elif 'open college website':
         #   webbrowser.open("jngec.ac.in")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'search internet' in query:
            speak("Tell me what you wana search on internet")
            command = takeCommand().lower()
            webbrowser.open(f"{command}")

        elif"send message" in query:
            kit.sendwhatmsg("+918219797170"," this is testing protocol",15,13)

        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'C:\\Users\\user\\Music\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))]

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") #  Hour Minutes Second these specifiers helps us to get time in string formmat
            speak(f"Sir, the time is {strTime}")

       # elif 'play game' in query:
        #    codePath="C:\\Users\\user\Desktop\\New folder\\demo for project by praveen"
         #   os.startfile(codePath)

       # elif 'open visual code' in query:
           # codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            #os.startfile(codePath)

        elif 'email to ' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "praveen.jngec@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend praveen bhai. I am not able to send this email")

