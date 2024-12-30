'''
Para este proyecto, crearemos una API RESTful con FastAPI que simula un servicio de pronóstico del tiempo 
simple. Esta API permitirá a los usuarios solicitar un pronóstico del tiempo para una ciudad específica 
durante un período de 3 días. Además, los usuarios pueden recuperar el pronóstico del tiempo para un día 
específico dentro de este período. El propósito de este proyecto es presentarte el desarrollo de API con 
FastAPI, que es un marco web moderno, rápido (de alto rendimiento) para crear API con Python 3.6 y 
versiones posteriores.

Resultado esperado
El usuario puede consultar los datos de pronóstico de 3 días para diferentes ciudades
Por ejemplo, al visitar http://127.0.0.1:8000/forecast/London se obtendrán los pronósticos de 3 días
El usuario también puede consultar un día determinado en los próximos 3 días. Por ejemplo, al consultar 
el día 2 visitando http://127.0.0.1:8000/forecast/London/2 se obtendrán los datos

Para simplificar, estamos generando datos falsos. Aquí tienes una estructura del código para empezar:

from fastapi import FastAPI
from random import randint, choice

app = FastAPI()

# Condiciones meteorológicas de muestra para simulación
weather_conditions = ["Soleado", "Nublado", "Lluvioso", "Tormentoso", "Nevando"]

@app.get("/forecast/{city_name}")
async def get_weather_forecast(city_name: str):
"""Obtén un pronóstico meteorológico de 3 días para una ciudad específica."""
...

return {"city": city_name, "forecasts": forecast_data}

@app.get("/forecast/{city_name}/{day}")
async def get_specific_day_forecast(city_name: str, day: int):
"""Obtén el pronóstico para un día específico en el rango de 3 días."""
...

return {"city": city_name, "forecast": forecast}

Requisitos previos
Bibliotecas requeridas: fastapi, unicorn
pip install fastapi uvicor

Para ejecutar la API, debe ejecutar: uvicorn clima_FastAPI:app --reload

donde wclima_FastAPI es el nombre de su script de Python y app es el nombre de la variable asociada a 
la instancia FastAPI().
'''

from fastapi import FastAPI
from random import randint, choice

app = FastAPI()

# Condiciones meteorológicas de muestra para simulación
weather_conditions = ["Soleado", "Nublado", "Lluvioso", "Tormentoso", "Nevando"]

def generate_forecast():
    """Genera un pronóstico de 3 días con condiciones aleatorias."""
    return [
        {"day": i + 1, "condition": choice(weather_conditions), "temperature": randint(15, 30)}
        for i in range(3)
    ]

@app.get("/forecast/{city_name}")
async def get_weather_forecast(city_name: str):
    """Obtén un pronóstico meteorológico de 3 días para una ciudad específica."""
    forecast_data = generate_forecast()
    return {"city": city_name, "forecasts": forecast_data}

@app.get("/forecast/{city_name}/{day}")
async def get_specific_day_forecast(city_name: str, day: int):
    """Obtén el pronóstico para un día específico en el rango de 3 días."""
    if day < 1 or day > 3:
        return {"error": "El día debe estar en el intervalo de 1 a 3."}
    
    forecast_data = generate_forecast()
    forecast = forecast_data[day - 1]  # Accede al pronóstico del día específico
    
    return {"city": city_name, "forecast": forecast}