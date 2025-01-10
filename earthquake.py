'''
Este proyecto obtiene datos de terremotos en tiempo real de la API del Servicio Geológico 
de los Estados Unidos (USGS) y muestra los 10 terremotos más fuertes de la semana pasada. 
Proporciona información útil sobre los terremotos más poderosos del mundo.

El programa realiza una solicitud de API a la API del Servicio Geológico de los Estados Unidos
en el siguiente endpoint: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson

Ese enlace devuelve los terremotos globales durante la semana actual. Luego, el programa muestra
los 10 terremotos más fuertes de la semana, mostrando información como la ubicación y el enlace del
terremoto para obtener más información sobre ese terremoto en particular.

'''

import requests
import json

# Hacer una solicitud de API a la API del Servicio Geológico de los Estados Unidos
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"
response = requests.get(url)

# Cargar los datos JSON de la respuesta
data = json.loads(response.text)

# Obtener la lista de terremotos de la semana
terremotos = data["features"]

# Crear una lista de terremotos con magnitudes y ubicaciones
terremotos_info = []
for terremoto in terremotos:
    magnitud = terremoto["properties"]["mag"]
    lugar = terremoto["properties"]["place"]
    terremotos_info.append((magnitud, lugar))

# Ordenar la lista de terremotos por magnitud
terremotos_info.sort(reverse=True)

# Mostrar los 10 terremotos más fuertes de la semana
print("Los 10 terremotos más fuertes de la semana:")
for i in range(10):
    magnitud, lugar = terremotos_info[i]
    print(f"{i + 1}. Magnitud: {magnitud}, Lugar: {lugar}")

# Obtener el enlace del terremoto para obtener más información
terremoto_num = int(input("Ingrese el número de un terremoto para obtener más información: "))
if 1 <= terremoto_num <= 10:
    enlace = terremotos[terremoto_num - 1]["properties"]["url"]
    print(f"Enlace del terremoto: {enlace}")
else:
    print("Número de terremoto inválido. Por favor, ingrese un número del 1 al 10.")

# Preguntar al usuario si desea obtener más información sobre un terremoto
respuesta = input("¿Desea obtener más información sobre otro terremoto? (s/n): ")
while respuesta.lower() == "s":
    terremoto_num = int(input("Ingrese el número de un terremoto para obtener más información: "))
    if 1 <= terremoto_num <= 10:
        enlace = terremotos[terremoto_num - 1]["properties"]["url"]
        print(f"Enlace del terremoto: {enlace}")
    else:
        print("Número de terremoto inválido. Por favor, ingrese un número del 1 al 10.")
    respuesta = input("¿Desea obtener más información sobre otro terremoto? (s/n): ")

print("Gracias por usar el programa. ¡Hasta luego!")