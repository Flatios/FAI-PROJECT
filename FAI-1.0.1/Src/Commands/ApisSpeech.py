
import Src.Module.Api as Api

def main(voice, name ,speak, city, town, country):
    if "hava durumu" in voice:
        havadurumu = Api.HavaDurumu(city1=city, town1=town, country1=country)
        speak(f"Gün: {havadurumu[0]} sıcaklık: {havadurumu[1]} hava: {havadurumu[2]}")
        
    if "haberler" in voice:
        Haberler = Api.Haberler(country1="tr")
        speak(f"başlık: {Haberler[0]} kaynak: {Haberler[1]}")
        
    if "nöbetçi eczane" in voice:
        ne = Api.NöbetciEczane(city1="Samsun", town1="çarşamba")
        speak(f"Nöbetçi eczane: {ne[0]} adres: {ne[1]}")
        