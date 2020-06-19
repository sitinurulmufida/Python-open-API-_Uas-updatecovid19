import requests
import json
import time

req = requests.get("https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/1/query?where=UPPER(Country_Region)%20like%20%27%25INDONESIA%25%27&outFields=Last_Update,Recovered,Deaths,Confirmed&returnGeometry=false&outSR=4326&f=json")
api = json.loads(req.content)

updateCorona = api['features'][0]['attributes']

print("\n\nUpdate Virus Covid-19")
print(time.ctime())
print("="*20)

print("Jumlah Pasien Positif Covid19 >>>", updateCorona['Confirmed'],"Orang")
print("Jumlah Pasien Yang Sembuh Covid19 >>>", updateCorona['Recovered'],"Orang")
print("Jumlah Pasien Meninggal Dunia Covid19 >>>", updateCorona['Deaths'],"Orang")

print()