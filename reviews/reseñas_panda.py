'''
Cree un programa para analizar los datos de las reseñas de los clientes con pandas y nltk. 
El programa cargará los datos de las reseñas, realizará una limpieza de texto y un análisis 
de sentimientos, y resumirá los datos calculando las calificaciones promedio de las reseñas 
positivas, neutrales y negativas. Este proyecto demostrará el procesamiento de datos, el 
procesamiento del lenguaje natural y la extracción de información mediante puntuaciones de 
sentimientos.

Vea a continuación lo que debería mostrar el programa cuando lo ejecute. El programa detecta 
el sentimiento (positivo, neutral o negativo) de cada comentario y muestra la calificación 
promedio de cada uno de los tres sentimientos diferentes. También imprime los datos.

Requisitos previos
Bibliotecas necesarias: pandas, nltk
pip install nltk pandas

Archivos necesarios: Descargue el archivo CSV que se proporciona más arriba.
'''

import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Descargar el recurso necesario para el análisis de sentimientos
nltk.download('vader_lexicon')

# Cargar los datos de las reseñas
data = pd.read_csv('.//reviews//reviews.csv')

# Mostrar los datos originales
print("Datos originales:")
print(data)

# Inicializar el analizador de sentimientos
sia = SentimentIntensityAnalyzer()

# Función para clasificar el sentimiento
def categorize_sentiment(review):
    score = sia.polarity_scores(review)['compound']
    if score >= 0.05:
        return 'positivo'
    elif score <= -0.05:
        return 'negativo'
    else:
        return 'neutral'

# Aplicar el análisis de sentimientos
data['sentiment'] = data['review'].apply(categorize_sentiment)

# Calcular la calificación promedio para cada sentimiento
data['rating'] = pd.to_numeric(data['rating'])
avg_ratings = data.groupby('sentiment')['rating'].mean()

# Mostrar resultados
print("\nCalificaciones promedio por sentimiento:")
print(avg_ratings)

# Mostrar los datos con el sentimiento agregado
print("\nDatos con sentimientos clasificados:")
print(data)