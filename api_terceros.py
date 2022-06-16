import requests
#from main import -> no se si es así o al reves
from poo import Pelicula

#apikey=98492397

base_url = "https://www.omdbapi.com/"

#http_rsp = requests.get(base_url, params={"apikey": 98492397, "t": })
#input/lista de imputs, como se pondrían varios? con el &?
#como se agrega el "&" para los parametros

###ej
titulo = input("titulo de la peli >>")
params = {"apikey": 98492397, "t": titulo}
http_resp = requests.get(base_url, params=params)
http_json = http_resp.json()

peli = []
for p in http_json:
    peli.append(Pelicula(p["Title"], p["Genre"], p["Released"], p["Rated"], p["Runtime"], p["Director"], p["Plot"]))
    print(f"Película recomendada: {peli}")
