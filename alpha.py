

import datetime
import os
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    speak("This is your personal assistant Alpha.")

    speak("How may I help you sir !")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.3
        r.energy_threshold = 1800
        r.operation_timeout = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'search' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching wikipedia..')
            query = query.replace("search", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)



        # time
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)
        
        # date
        elif 'date' in query:
            strDate = datetime.datetime.now().strftime("%A:%d:%B:%Y")
            speak(f"Sir, todays date is {strDate}")
            print(strDate)
        
        # open files/folders
        elif 'open class' in query:
            classpath = "F:\class"
            speak('opening Class')
            os.startfile(classpath)        

        elif 'mechanics' in query:
            EMpath = "G:\class\EM"
            speak('getting Mechanics')
            os.startfile(EMpath)

        elif 'physics' in query:
            PHYpath = "G:\class\PHY"
            speak('getting physics')
            os.startfile(PHYpath)

        elif 'mathematics' in query:
            MATHSpath = "G:\class\\Math"
            speak('getting Maths')
            os.startfile(MATHSpath)




        # MEDIA --------MEDIA------------MEDIA

        elif 'movies' in query:
            MATHSpath = "G:\Movies"
            speak('getting movies')
            os.startfile(MATHSpath)

        elif 'wonder woman' in query:
            MATHSpath = "G:\Movies\\Wonder Woman 1984 - 2020 WebRip 720p IMAX [Hindi Cam 2.0 + English 5.1] AAC x264 ESub - mkvCinemas [Telly].mkv"
            speak('playing wonder woman 1984')
            os.startfile(MATHSpath)

        elif 'crackdown 1' in query:
            MATHSpath = "G:\Movies\Crackdown (2020) 720p Voot Hindi 720p WEBRip x264 AAC. ESub\\Crackdown E01.mkv"
            speak('playing crackdown part 1')
            os.startfile(MATHSpath)

        elif 'crackdown 2' in query:
            MATHSpath = "G:\Movies\Crackdown (2020) 720p Voot Hindi 720p WEBRip x264 AAC. ESub\\Crackdown E02.mkv"
            speak('playing crackdown part 2')
            os.startfile(MATHSpath)




        # youtube

        elif 'play' in query:
            stuff = query.replace('play', '')
            speak('playing ' + stuff)
            pywhatkit.playonyt(stuff)

        
        # joke
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        # google search
        elif 'google' in query:
            cm = query.replace('google', '')
            speak('getting' + cm)
            pywhatkit.search(cm)

            
        # Open files
        elif 'logo' in query:
            MATHSpath = "E:\\frontender\images\logo.png"
            speak('getting logo')
            os.startfile(MATHSpath)


        elif 'front' in query:
            MATHSpath = "E:\\frontender\\index.html"
            speak('getting site')
            os.startfile(MATHSpath)

        elif 'whatsapp' in query:
            MATHSpath = "E:\\soft\\WhatsAppSetup.exe"
            speak('getting whatsapp')
            os.startfile(MATHSpath)

        elif 'telegram' in query:
            MATHSpath = "E:\\ak2\\Telegram Desktop\\Telegram.exe"
            speak('getting telegram')
            os.startfile(MATHSpath)


        # conversation--------conv-----conv

        elif 'hello' in query:
            speak('hello A.K.')


        elif 'hey' in query:
            speak('are you looking for me sir!')



        elif 'how are you' in query:
            speak('fine and energetic')


         # program close

        elif 'exit' in query:
            speak('Good bye sir')
            break
