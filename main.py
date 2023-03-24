import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import  pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    # engine.say("what can I do for you...")
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                # talk(command)
    except:
        pass
    return command

def run_commandAlexa():
    command = take_command()
    print(command)
    if 'play' in command:
        # talk('playing....')
        song = command.replace('play','')
        talk('playing...' + song)
        # print("playing...")
        pywhatkit.playonyt(song)
    elif 'time' in command :
        time = datetime.datetime.now().strftime('%I: %M %p')
        talk('current time is...'+time)
        print(time)
    elif 'who is' in command:
        person = command.replace('who is','')
        result = wikipedia.summary(person,1)
        talk(result)
        print(result)
    elif 'what is' in command:
        process_or_thing = command.replace('what is','')
        result = wikipedia.summary(process_or_thing,1)
        talk(result)
        print(result)
    elif 'date' in command:
        talk("sorry, i am a program not a human being..")
    elif 'are you single' in command:
        talk("sorry, I haven't a heart which make me emotional")
    elif 'joke' in command:
        print(pyjokes.get_jokes())
        talk(pyjokes.get_jokes())
    elif 'jokes in hindi' in command:
        joke = pyjokes.get_jokes()
        talk(joke)
    else:
        talk('please , say the command again...')

while True:
    run_commandAlexa()
