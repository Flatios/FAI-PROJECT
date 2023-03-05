import os
import playsound

# Musics

phonk = "Src/Module/Musics/Phonk/phonk1.mp3"

chill = "Src/Module/Musics/Chill/Chill1.mp3"



# Sounds
Ding = "Src/Module/Musics/Sounds/DING.mp3"

# Komik

zort = "Src/Module/Musics/Sounds/zort.mp3"


# ---------------------------------------------------------------------------

def Musics(music):
    if music == "phonk":
        playsound.playsound(phonk)
        return
    if music == "chill":
        playsound.playsound(chill)
        return
    if music == "zort":
        playsound.playsound(zort)
        return
    if music == "DING":
        playsound.playsound(Ding)    
        return
        
# Musics(music='Name') # Örn Name = phonk