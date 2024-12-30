'''
Este proyecto extrae los colores dominantes de cualquier imagen y crea una paleta de colores.
Utiliza OpenCV para cargar la imagen y la agrupación en clústeres KMeans de scikit-learn para 
encontrar los colores principales. Este proyecto le enseñará sobre algoritmos de agrupación en 
clústeres y procesamiento de imágenes, al mismo tiempo que produce resultados visualmente atractivos.
Resultado esperado
El programa lee un archivo image.png. Después de ejecutar el programa, debería generar y mostrar la 
paleta de colores para la imagen de entrada utilizando matplotlib.

Requisitos previos
Bibliotecas requeridas: opencv, numpy, scikit-learn, matplotlib
pip install opencv-python numpy scikit-learn matplotlib
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Cargar la imagen
image = cv2.imread('image.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convertir de BGR a RGB

# Redimensionar la imagen a un tamaño más manejable
image = image.reshape((image.shape[0] * image.shape[1], 3))

# Aplicar KMeans para encontrar los colores dominantes
n_colors = 5  # Número de colores que deseas extraer
kmeans = KMeans(n_clusters=n_colors)
kmeans.fit(image)

# Obtener los colores
colors = kmeans.cluster_centers_.astype(int)

# Crear una paleta de colores
palette = np.zeros((50, 300, 3), dtype=int)

for i, color in enumerate(colors):
    palette[:, i * 60:(i + 1) * 60] = color  # Cada color ocupa un bloque de 60 píxeles

# Mostrar la paleta usando Matplotlib
plt.imshow(palette)
plt.axis('off')  # No mostrar los ejes
plt.show()