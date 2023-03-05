import os
from colorama import Fore, Back, Style 
import time
import requests
from requests.exceptions import ConnectionError
import pyfiglet

Fore.RESET = Style.RESET_ALL
os.system('cls||clear')


def main():
    result = pyfiglet.figlet_format("Flatios INC")
    print(result)
    print(Fore.YELLOW + "Starting...")
    print("Speech Dosyası Kontrol Ediliyor...")
    while os.path.exists("Speech.mp3") :
        print("Speech Dosyası Mevcut Siliniyor")
        os.remove("Speech.mp3")
        InternetControl()
    else:
        print("Speech Dosyası Mevcut Değil")
        InternetControl()
        

    
    
def InternetControl():
    try:
        requests.get('https://www.google.com')
    except requests.ConnectionError:
        Error('Connection Error')
    else:
        print(Fore.GREEN + "Internet Connection Success")
        apicontrol()
    
def apicontrol():
    try:
        requests.get("https://collectapi.com/tr/")
    except requests.ConnectionError:
        Error('Connection Error')
    else:
        print(Fore.GREEN + "Api Connection Success")
        Start()    
        
def Start():
    yn = input(Fore.YELLOW + "Sistemi Başlatmak İstiyormusunuz Y/N: ")
    
    if yn == 'Y' or yn == 'yes' or yn == 'y':
        print(Fore.GREEN + "Start Success")
        import Src.FAI as AI
    else:
        Error("Start Failed")
        Fore.RESET = Style.RESET_ALL
        exit()
        
    

        
def Error(Error):
    print(f'{Fore.RED}Hata >> {Error}')
    Fore.RESET = Style.RESET_ALL
    exit()
    


main()