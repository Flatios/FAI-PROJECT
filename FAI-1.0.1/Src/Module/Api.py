import os 
import requests
import json

collectapi_key1 = "apikey 1BGRyFDxr6Loplp3Kstpj8:4cqd5f14HGSXM8G3AIIRwm"
collectapi_key2 = "apikey 64bcQbiIEeEoCjD7O0VuLW:3KPS7SfRJgppiAZv76e4FT"


def HavaDurumu(city1, town1, country1):
        url = f"http://api.collectapi.com/weather/getWeather?data.lang={country1}&data.city={city1}"
        headers = {
            'content-type': "application/json",
            'authorization': collectapi_key2
            }
        response = requests.request("GET", url, headers=headers)
        result = json.loads(response.text)
        for HD1 in result["result"]:
          HD_gün = HD1['day']     
          HD_sıcaklık = HD1['degree']
          HD_açıklama = HD1['description']
          return HD_gün, HD_sıcaklık, HD_açıklama

def Haberler(country1):
        url = f"http://api.collectapi.com/news/getNews?country={country1}&tag=general"
        headers = {
            'content-type': "application/json",
            'authorization': collectapi_key1
            }
        response = requests.request("GET", url, headers=headers)
        result = json.loads(response.text)
        for H in result['result']:
          name = H['name']     
          source = H['source']
          return name, source
        
def NöbetciEczane(city1, town1):
        url = f"http://api.collectapi.com/health/dutyPharmacy?ilce={town1}&il={city1}"
        headers = {
            'content-type': "application/json",
            'authorization': collectapi_key1
            }
        response = requests.request("GET", url, headers=headers)
        result = json.loads(response.text)
        for H in result['result']:
          name = H['name']     
          adres = H['address']
          return name, adres
        
        
def Server():
    url = f"https://fmcsl.000webhostapp.com/flatioapp/FAI.json"
    headers = {
        'content-type': "application/json",
    }
    response = requests.request("GET", url, headers=headers)
    result = json.loads(response.text)
    for Srv in result['result']:
      return Srv
            