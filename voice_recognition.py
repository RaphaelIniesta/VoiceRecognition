# importing libraries 
from linecache import getline
from platform import release
import speech_recognition as sr 
import pyttsx3
from pyautogui import *
import time

def Recognition():
    r = sr.Recognizer()

    # Use microphone as input device
    with sr.Microphone() as source:
        # Adjusting to ambient noise
        #print("Please, stay silent. Calibrating background noise")
        r.adjust_for_ambient_noise(source, duration=6)
        print("What's your answer?")

        audio2 = r.listen(source)
        # In 'language' you can change the recognition language. the defaul is US english
        # You can find a list of the languages here 
        # -> https://stackoverflow.com/questions/14257598/what-are-language-codes-in-chromes-implementation-of-the-html5-speech-recogniti
        txt = r.recognize_google(audio2, language = "en-US")
        txt = txt.lower()

    commands = txt.split(' ')

    #print(txt)
    return commands