import os 



def Windows():
  try:
    from colorama import Fore, Back, Style
    import gtts
    import playsound
    import requests
    import speech_recognition
    import pyaudio
    import pyfiglet
  except ModuleNotFoundError:
    print("not found Module not found")
    os.system("pip install gTTS")
    os.system("pip install playsound==1.2.2")
    os.system("pip install requests")
    os.system("pip install SpeechRecognition")
    os.system("pip install colorama")   
    os.system("pip install pyaudio")
    os.system("pip install pyfiglet")
    
    
  else:
    print(Fore.GREEN + "Successfully Modules Found") 
     
  
def Linux():
  try:
    from colorama import Fore, Back, Style
    import gtts
    import playsound
    import requests
    import speech_recognition
    import pyaudio
    import pyfiglet
  except ModuleNotFoundError:
    print("not found downloading modules...")
    os.system("sudo apt-get install -y flac")
    os.system("sudo apt-get install -y mpg321")
    os.system("pip install gTTS")
    os.system("pip install requests")
    os.system("pip install SpeechRecognition")
    os.system("pip install colorama")  
    os.system("pip install pyaudio")
    os.system("pip install pyfiglet")
  else:
    print(Fore.GREEN + "Successfully Modules Found")    



if os.name == "nt":
  Windows()
if os.name == "posix":
  Linux()

if os.name == "macosx":
  print("Mac OS is not supported")


  
