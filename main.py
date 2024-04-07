import speech_recognition as sr
import wikipedia
import webbrowser
from pytube import YouTube
import pyttsx3
import datetime
import re
from math import *
import vlc
import os

def telltime():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def takecommand():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            query = r.recognize_google(audio)
            print(f"User said: {query}")
            return query.lower()
    except sr.RequestError:
        print("Internet connection is not available.")

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def hello():
    speak("Hi! I am zeeobot build and brought up by Miss Sara Kazi and team how can i assist you ?")

def takeQuery():
    hello()
    while True:
        query = takecommand()
        if 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/watch?v=qL3s44rk7B8")
        elif 'open java tutorial' in query:
            webbrowser.open("https://www.javatpoint.com")
        elif 'introduce the head of your branch' in query:
            speak("Sure, let me introduce you to the head of our department Meet Mr.Ali Karim Sayyed, a seasoned professional at the forefront of Artificial Intelligence and machine learning With over a decade of dedicated experience in the field, Mr. Sayyed has honed his expertise as the Head of Department in this dynamic domain.His journey began with a Master's in Computer Engineering, followed by a specialized Master's degree in Artificial Intelligence and Machine Learning from the prestigious UK.Beyond his academic achievements, Mr. Sayyed is a prolific author, having penned four insightful books published by Nirali Prakashan. His passion for advancing knowledge and his commitment to the field shine through his contributions, making him a respected figure in the industry. ")
        elif 'introduce your project guide' in query:
            speak("Allow me to introduce Miss Zikra, our esteemed project guide and a beacon of guidance in our academic endeavors. With her wealth of experience and unwavering dedication, Miss Zikra embodies the essence of mentorship and inspiration.In her role as our project guide, Miss zikra brings a unique blend of expertise, creativity, and passion to the table. With a background in BE in Computer engineering Beyond her impressive credentials, Miss Shaikh is known for her approachable demeanor and genuine interest in our success. Her ability to foster an environment of collaboration and innovation empowers each team member to excel and contribute meaningfully to our project.")
        elif 'tell me current time' in query:
            telltime()
        elif 'wikipedia' in query:
            speak("Checking Wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            speak(result)
        elif 'calculate' in query:
            expression = re.search(r'calculate (.+)', query).group(1)
            result = calculate(expression)
            speak(f"The result is {result}")

        elif 'exit' in query:
            speak("Goodbye!")
            break

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)

def recognize_speech(prompt):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(prompt)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio")
    except sr.RequestError:
        print("Could not request results from Google Web Speech API")
    return ""

def play_youtube_audio(video_url):
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(filename="temp_audio.mp4")

    player = vlc.MediaPlayer("temp_audio.mp4")
    player.play()
    while player.is_playing():
        pass
    os.remove("temp_audio.mp4")

if __name__ == "__main__":
    takeQuery()
    # Capture audio from the microphone and recognize speech
    speech = recognize_speech("How can I assist you?")
    print("You said:", speech)

    if "open YouTube" in speech:
        webbrowser.open("https://www.youtube.com")
    elif "play music" in speech:
        # Replace with the actual YouTube video URL of the music you want to play
        youtube_url = "https://www.youtube.com/watch?v=0hz5jzemqJ0"
        play_youtube_audio(youtube_url)
    else:
        print("Command not recognized.")
