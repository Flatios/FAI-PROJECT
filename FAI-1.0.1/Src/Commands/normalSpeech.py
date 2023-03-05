import os
import random
import time

import Src.Module.Musics.Musics as M
import Src.Module.Api as Api

def main(voice, name ,speak, city, town, country):
    if "merhaba" in voice:
        speak("Merhaba " + name)

    if "selam" in voice:
        speak("aleykümselam " + name)     

    if "müzik çal" in voice:
        speak("Random Müzik Çalınıyor " + name)
        seçim_M = ['chill', 'phonk']
        random_m = random.choice(seçim_M)
        M.Musics(music=random_m)
        return True
    
    if "saat kaç" in voice:
        time_live = time.strftime("%H:%M")
        rsa = ['Ben saat mi satıyorum', f'Saat: {time_live}'] 
        rs = random.choice(rsa)   
        speak(rs)

    if "seni kim programladı" in voice or "seni kim yaptı" in voice or "seni yapan kim" in voice:
        speak("Hakan Kaygusuz İletişim İçin: hakankaygusuzone@gmail.com")
