# PIP Modules

from gtts import gTTS
import os
import random
import speech_recognition as sr 
import time

# My Modules


import Src.Module.Musics.Musics as msc

import Src.Commands.adminSpeech as cmdAD
import Src.Commands.normalSpeech as NS
import Src.Commands.funnySpeech as k
import Src.Commands.ApisSpeech as Ap


#Define
country = "tr"
city = "samsun"
town = "çarşamba"
r = sr.Recognizer()

# Record and Recognize
def record():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)  
        audio = r.listen(source)
        voice1 = ""
        try:
            voice1 = r.recognize_google(audio, language="tr-TR")
            print(f"User: {voice1}")
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım")
        except sr.RequestError:
            print("Asistan: Sistem çalışmıyor")
        return voice1

    
# Commands
def response(voice1):
    cmdAD.main(voice=voice1, name=name1, country=country, city=city, town=town, speak=speak)
    NS.main(voice=voice1, name=name1, country=country, city=city, town=town, speak=speak)
    k.main(voice=voice1, name=name1, country=country, city=city, town=town, speak=speak, record1=record)
    Ap.main(voice=voice1, name=name1, country=country, city=city, town=town, speak=speak)

        
#Speaking
def speak(string):
    print("Asistant: " + string)
    gtts = gTTS(text=string, lang='tr', slow=False)
    file = 'Speech.mp3'
    gtts.save(file) 
    if os.name == "nt":
        from playsound import playsound
        playsound(file)
        os.remove(file)
    if os.name == "posix":
        os.system("sudo mpg321 " + file)
        os.remove(file)
    if os.name == "macosx":
        print("Mac OS is not supported")
        
# TEST
def test(wake):
    if "jessica" in wake:
        speak("efendim " + name1)
        wake = record()
        if wake != '':
            voice1 = wake.lower()
            response(voice1)

print("FAI IS Started")
            
#WHILE
            
while True:
    name1 = " "
    wake = record()
    if wake != '':
        wake = wake.lower()
        test(wake)