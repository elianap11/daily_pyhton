'''
Hoy crearemos la siguiente aplicación web de panel meteorológico:
Los usuarios pueden buscar una ciudad en el cuadro de texto y la información meteorológica actual de esa ciudad se mostrará debajo del botón.

Puede utilizar la API Open Weather para obtener datos meteorológicos actuales. Debe registrarse para obtener una cuenta gratuita y obtener una clave API. Luego, cree una aplicación web Flask que realice solicitudes API al punto final http://api.openweathermap.org/data/2.5/weather y muestre los datos JSON recibidos en la página web.

Para ayudarte a resolver este proyecto, aquí tienes el script de un proyecto similar anterior en el que creamos una aplicación de línea de comandos para obtener el clima actual de cualquier ciudad mediante la API Open Weather:

import requests

# Reemplazar con la clave de API de OpenWeatherMap
API_KEY = "?"

def get_temperature(city):
"""Obtiene la temperatura actual de una ciudad determinada.

Args:
city: El nombre de la ciudad para la que se obtendrán los datos meteorológicos.

Retornos:
Una cadena que contiene la temperatura actual en grados Celsius o None si se produce un error.
"""
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)

if response.status_code == 200:
data = response.json()
temp = data["main"]["temp"]
return f"Temperatura actual en {ciudad}: {temp:.1f}°C"
else:
print(f"Error: {response.status_code}")
return None

if __name__ == "__main__":
ciudad = input("Ingrese la ciudad: ")

temperatura = get_temperature(ciudad)
if temperatura:
print(temperatura)
else:
print("Error al recuperar la temperatura.")

'''

import requests
from flask import Flask, request, render_template

app = Flask(__name__)

# Reemplazar con la clave de API de OpenWeatherMap
API_KEY = ""

@app.route('/', methods=['GET', 'POST'])    
def index():            
    if request.method == 'POST':
        ciudad = request.form['ciudad']
        temperatura = get_temperature(ciudad)
        return render_template('index.html', temperatura=temperatura)
    return render_template('index.html')

def get_temperature(ciudad):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:        
        data = response.json()
        temp = data["main"]["temp"]
        return f"Temperatura actual en {ciudad}: {temp:.1f}°C"
    else:
        return None                

if __name__ == '__main__':
    app.run(debug=True) # Ejecutar la aplicación en modo de depuración      