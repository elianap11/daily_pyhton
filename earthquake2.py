'''
En el proyecto anterior, extrajimos los 10 terremotos más fuertes del mundo durante
la semana actual. Hoy ampliaremos este proyecto aún más mostrando los terremotos 
globales en un mapa con Python.
De manera similar al proyecto anterior, el programa realiza una solicitud a la API 
del Servicio Geológico de los Estados Unidos en el siguiente endpoint para obtener 
todos los terremotos que ocurrieron durante la semana actual:
https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson
El programa traza las ubicaciones de los terremotos en un mapa mundial interactivo utilizando Folium.
'''

import requests
import json
import folium

# Hacer una solicitud de API a la API del Servicio Geológico de los Estados Unidos
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"
response = requests.get(url)

# Cargar los datos JSON de la respuesta
data = json.loads(response.text)

# Obtener la lista de terremotos de la semana
terremotos = data["features"]

# Crear un mapa mundial interactivo con Folium
mapa = folium.Map(location=[0, 0], zoom_start=2)

# Agregar marcadores al mapa para cada terremoto
for terremoto in terremotos:
    lugar = terremoto["properties"]["place"]
    magnitud = terremoto["properties"]["mag"]
    latitud = terremoto["geometry"]["coordinates"][1]
    longitud = terremoto["geometry"]["coordinates"][0]
    folium.Marker([latitud, longitud], popup=f"{lugar}, Magnitud: {magnitud}").add_to(mapa)

# Guardar el mapa como un archivo HTML
mapa.save("terremotos_globales.html")

print("Mapa de los terremotos globales de la semana guardado como 'terremotos_globales.html'.")
print("Abre el archivo HTML en tu navegador para ver el mapa interactivo.")

# Preguntar al usuario si desea obtener más información sobre un terremoto
respuesta = input("¿Desea obtener más información sobre un terremoto? (s/n): ")
while respuesta.lower() == "s":
    terremoto_num = int(input("Ingrese el número de un terremoto para obtener más información: "))
    if 1 <= terremoto_num <= len(terremotos):
        enlace = terremotos[terremoto_num - 1]["properties"]["url"]
        print(f"Enlace del terremoto: {enlace}")
    else:
        print("Número de terremoto inválido. Por favor, ingrese un número válido.")
    respuesta = input("¿Desea obtener más información sobre otro terremoto? (s/n): ")
