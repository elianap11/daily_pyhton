'''
La tarea es analizar datos de IMDb sobre películas, sus géneros, años de estreno, 
calificaciones y más. Descarga el archivo movies.csv. El objetivo es visualizar las
calificaciones de las películas a partir de los datos proporcionados en el archivo 
CSV. El programa debe generar una distribución de calificaciones de películas. El 
gráfico debe mostrar la frecuencia de cada calificación. Por ejemplo, las 
calificaciones 8.5 y 8.6 son las más frecuentes en el archivo CSV. Recomendamos usar 
pandas, matplotlib y seaborn para generar el gráfico anterior.
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

movies_data = pd.read_csv('movies.csv')

print(movies_data.head())  
print(movies_data.columns)

if 'Rating' in movies_data.columns:
    
    plt.figure(figsize=(10, 6))
    sns.histplot(movies_data['Rating'], bins=30, kde=True)  # kde=True añade una curva de densidad
    plt.title('Distribución de Calificaciones de Películas')
    plt.xlabel('Calificación')
    plt.ylabel('Frecuencia')
    plt.xlim(0, 10)  # Asumiendo que las calificaciones están en el rango de 0 a 10
    plt.grid()
    plt.show()
else:
    print("La columna 'Rating' no se encuentra en el archivo CSV.")
