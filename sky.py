''' Basic python coding for sky(voice assistant name) bot'''


#import libraries

import logging
from flask import Flask, render_template, redirect
from flask_cors import cross_origin
import speech_recognition as sr
import pyttsx3
import datetime
import pyjokes
import webbrowser
import wikipedia
import names



listener = sr.Recognizer()

#logging function
def logging_fun():
    logging.basicConfig(filename= "sky.txt",level=logging.INFO,format='%(asctime)s %(message)s')


#voice assistant reply
def engine_talk(text):
    #logging.info("we are inside engine talk function voice assistant ready speak")
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    #logging.info('user got his output')

# input from user as his/her voice
def user_commands():
    #logging.info("we are inside user_commands function")
    #logging.info("voice assistant got your command")

    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'sky' in command:
                command = command.replace('sky', '')
    except:
        pass
    return command

#voice assistant output function
def run_sky():
    import pywhatkit
    #logging_fun()
    #logging.info("inside run_sky function")
    try:
        engine_talk('how can i help you')
        #logging.info("voice assistant ready for your command")
        command = user_commands()


        # most asked question from google Assistant
        if 'hello' in command:
            engine_talk("hello sir")
        elif 'how are you' in command:
            engine_talk("I am fine, Thank you")
            engine_talk("How are you, Sir")
        elif 'fine' in command or "good" in command:
            engine_talk("It's good to know that your fine")
        elif "who i am" in command:
            engine_talk("If you talk then definitely your human")
        elif "why you came" in command:
            engine_talk("Thanks to Aman. further It's a secret")
        elif 'reason for you' in command:
            engine_talk("I was created as a Minor project by aman ")
        elif 'love' in command:
            engine_talk("It is 7th sense that destroy all other senses")
        elif "will you be my gf" in command or "will you be my bf" in command:
            engine_talk("I'm not sure about, may be you should give me some time")
        elif "i love you" in command:
            engine_talk("It's hard to understand")
        elif "who are you" in command or "what is your name" in command:
            engine_talk("I am sky your virtual assistant created by Aman Negi")
        elif 'why sky' in command or "why you got" in command or "why your name is sky" in command:
            engine_talk("because sky has no limits")
        elif "change your name" in command or 'can i give you' in command:
            engine_talk("What would you like to call me, Sir ")
        elif 'i will call you' in command:
            name=command.replace("i will call you","")
            engine_talk(name)
            engine_talk("nice name")
            engine_talk("Thanks for naming me")
        elif "what's your nick name" in command or "your nice name" in command:
            engine_talk("My friends call me three sixty degree")
        elif "who made you" in command or "who created you" in command:
            engine_talk("I have been created by Aman Negi")
        elif "name" in command or "nick name" in command:
            name=names.get_first_name()
            engine_talk(name)


        #current time
        elif 'time' in command:
            #logging.info("user asking for time")
            time = datetime.datetime.now().strftime('%I:%M %p')
            engine_talk('Current time is ' + time)
            logging.info("assitant got his output")


        #weather report
        elif 'weather' in command:
            #logging.info("user asking for weather report")
            place=command.replace('weather',"")
            engine_talk("weather of "+place)
            webbrowser.open("https://www.google.com/search?q="+place+"+weather")

        #jokes
        elif 'joke' in command:
            #logging.info("user wants a joke")
            get_j = pyjokes.get_joke()
            engine_talk(get_j)

        #wikipedia
        elif 'who is' in command or 'tell me about' in command:
            #logging.info("bot inside wikipedia")
            if 'who is' in command:
                person = command.replace('who is', '')
            else:
                person = command.replace('tell me about', '')
            info = wikipedia.summary(person, 1)
            engine_talk(info)
            #logging.info(info)

        #location
        elif "where is" in command:
            #logging.info("bot inside google map")
            query = command.replace("where is", "")
            location = query
            engine_talk("User asked to Locate"+location)
            webbrowser.open("https://www.google.com/maps/place/"+location+"/")


        #song,music,video on youtube
        elif 'play' in command :
            #logging.info("bot inside youtube")
            search=command.replace("play","")
            if 'play' not in search:
                engine_talk('here you go')
                pywhatkit.playonyt(search)

        #simple open google web browser
        elif 'open google' in command or 'search on google' in command:
            engine_talk("Here you go to Google\n")
            webbrowser.open("google.com")


        else:
            engine_talk("I didn't hear you properly")
    except:
        pass


# Api's
app = Flask("__name__")
@cross_origin()
@app.route('/')
def hello():
    return render_template("sky.html")


@app.route("/home")
@cross_origin()
def home():
    return redirect('/')


@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def submit():
    # use while loop here if you want your bot not get terminated after every action
    run_sky()
    return render_template("sky.html")



if __name__ == "__main__":
    app.run(debug=True,port=7000)