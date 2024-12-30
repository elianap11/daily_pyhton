'''
Creamos un programa que sugiere libros a los usuarios en función de la similitud 
de sus resúmenes de trama.

Resultado esperado
El programa permite al usuario proporcionar un resumen de la trama de un libro que 
le gustó en la terminal. A este usuario le gustó el libro “El capitán de la evolución”:

Luego, la aplicación recomienda los 5 libros más similares. Este proyecto implica el 
procesamiento del lenguaje natural y el análisis de similitud de texto. Los libros 
sugeridos por el programa se toman del archivo book.csv
'''
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Cargar los datos desde un archivo CSV
def load_books_from_csv(file_path):
    return pd.read_csv(file_path)

# Ruta del archivo CSV
file_path = "./resumenes_libros/books.csv"

# Crear DataFrame
books = load_books_from_csv(file_path)

# Instancia del vectorizador
tfidf_vectorizer = TfidfVectorizer()
tfidf = tfidf_vectorizer.fit_transform(books['Summary'])  # Vectorizar los resúmenes de libros una vez

# Función de recomendación
def recommend_books(user_summary):
    # Transformar el resumen del usuario
    user_vector = tfidf_vectorizer.transform([user_summary])  # Usa el mismo vectorizador ya ajustado
    
    # Calcular similitudes
    cosine_similarities = linear_kernel(user_vector, tfidf).flatten()
    similar_indices = cosine_similarities.argsort()[-5:][::-1]  # Obtener los 5 mejores

    # Obtenemos los libros más similares
    recommended_books = books.iloc[similar_indices]
    return recommended_books

# Solicitar input del usuario
user_summary = input("Escribe un resumen de la trama de un libro que te gustó: ")

# Llamar a la función de recomendación
recommendations = recommend_books(user_summary)

# Mostrar recomendaciones
print("Te sugerimos los siguientes libros:")
for index, row in recommendations.iterrows():
    print(f" - {row['Title']}: {row['Summary']}")