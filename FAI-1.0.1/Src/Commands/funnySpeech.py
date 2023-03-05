import os
import random

import Src.Module.Musics.Musics as M

ADMINLIST = ['hakan']



def main(voice, name ,speak, city, town, country, record1):
    if "zort" in voice:
        M.Musics(music="zort")
    if "bana fıkra anlat" in voice:
        fıkra = [
            'adamın biri sigara bırakma hattını aramış Demiş ki benim eve de iki tane sigara bırak', 
            'Adamın biri markette alışveriş yaparken, yanına yaklaşan bir kadın ona "Bir dakika bekleyebilir miyim? Ben sizin hayalini kurduğunuz kadınım. dedi. Adam cevap verdi "Maalesef hayalimdeki kadın sağır değildi.', 
            'Adamın biri yolda yürürken bir arkadaşıyla karşılaşır ve ona Nasılsın? diye sorar. Arkadaşı cevap verir İyiyim, sen nasılsın? Adam yanıt verir "Ben de iyiyim, ama senin kadar değil.'   
        ]
        fıkraa = random.choice(fıkra)
        speak(fıkraa)
    if "bana kötü espri yap" in voice:
        kötüespri = [
            'Burun kemiği kırık bir adam bir bara girer ve barmen ona "Ne içersin?" diye sorar. Adam cevap verir "Benim burun kemiğim kırık, belki bir Bloody Mary içebilirim." Barmen şöyle der: "Ama senin burun kemiğin yok ki!" Adam da yanıt verir: "Evet, tam olarak ne kadar kanıksamadığımı farkettin mi?"',
            'Neden bazı insanlar kahve ile evlenmek istemezler? Çünkü kahve sürekli filtreli ilişkilerden bıkmıştır ve artık French Press ile biraz baskın istiyor.',
            'Bir gün, bir doktor ve bir mühendis birlikte bir yolculuk yapıyorlarmış. Yolda bir kazaya karışmışlar ve hayatlarını kaybetmişler. Cenazeleri morga götürülmüş ve birkaç gün sonra morgun soğutma sistemi bozulmuş. Doktorun cesedi çürüyüp kötü kokular yaymaya başlamış, ancak mühendisin cesedi hiç bozulmamış. Bunun nedeni neymiş biliyor musunuz? Mühendis hiçbir zaman çalışmamıştı.',
        ]
        kötüespria = random.choice(kötüespri)
        speak(kötüespria)
    