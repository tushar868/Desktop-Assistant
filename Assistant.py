import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #for female voice try this -- voices[1]


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

    speak("Hello Sir. Please tell me how may I help you")       

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
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
  
        query = takeCommand().lower()

       
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "yourself" in query:
            speak("Okay,,")
            speak("I am Jack and i was created by Devil88")
            speak("I was a dream of a boy dreaming to make a perfect virtual assistant")
            speak("He soon established the company named Dragonspyder")
            speak("Slowly,I came to life")
            speak("I started learning various things like calculations,General knowldge etc etc")
            speak("Now I am capable of doing various things like Beatboxing,opening applications,Cracking jokes,Playing music etc.")
            speak("Okay,thats a wrap I wont say more ")


        elif 'open youtube' in query:
            speak("Okay")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Okay,What should i search on google")
            #webbrowser.open("google.com")
            #speak("Launching Google")
            cm=takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open facebook' in query:
            speak("Okay")
            webbrowser.open("facebook.com")
            speak("Launching facebook")

        elif 'open instagram' in query:
            speak("Okay")
            webbrowser.open("Instagram.com")
            speak("Launching instagram")

        elif 'play movies' in query:
            speak("Okay")
            video_dir = 'E:\\uuu\\Tejas.mp4' 
            os.startfile('Enter your movies directory (file path) hear')  


        elif 'play music' in query:
            speak("Okay")
            music_dir = 'Enter your music directory (file path) hear'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            speak("Okay")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'cyber attack' in query:
            speak("Okay")
            webbrowser.open("https://cybermap.kaspersky.com/")
            speak("Launching cyber attack") 

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "which you want to send@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email") 

        elif 'go offline' in query:
            speak("okay")
            speak("have a nice day sir....")   
            quit()
