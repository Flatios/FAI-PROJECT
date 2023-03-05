import Src.Module.Api as Api


ADMINLIST = ['hakan']



def main(voice, name ,speak, city, town, country):
    if name in ADMINLIST:
        if "sunuculara bağlan" in voice:
            speak("Merhaba ADMIN " + name + " Sunucuya Bağlanıyorum...")
            Srv = Api.Server()
            speak(Srv['FAI_Ver'])