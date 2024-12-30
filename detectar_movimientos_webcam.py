'''
En este proyecto, aprenderá a detectar movimiento en una transmisión de video y resaltar los objetos 
en movimiento. Esto se puede utilizar para aplicaciones como sistemas de vigilancia o edición de video 
automatizada. El movimiento se puede detectar con Python utilizando la biblioteca OpenCV al comparar 
fotogramas consecutivos de un video para detectar cambios o movimiento. Luego, resaltamos las regiones 
en el fotograma donde se detectó movimiento.

Cómo funciona el proyecto
El programa inicia la cámara web de la computadora y detecta movimiento
'''

import cv2
import numpy as np

# Inicializa la captura de video (0 para la cámara web)
cap = cv2.VideoCapture(0)

# Lee el primer fotograma y convierte a escala de grises
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    # Calcula la diferencia entre dos fotogramas
    diff = cv2.absdiff(frame1, frame2)

    # Convierte la imagen a escala de grises
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Aplica un umbral para binarizar la imagen
    _, thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)

    # Dilata la imagen para llenar agujeros
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Encuentra los contornos en la imagen dilatada
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Filtra los contornos por área
        if cv2.contourArea(contour) > 500:  # Cambia el umbral según sea necesario
            (x, y, w, h) = cv2.boundingRect(contour)
            # Dibuja un rectángulo alrededor de los objetos en movimiento
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Muestra el fotograma procesado
    cv2.imshow("Motion Detector", frame1)

    # Actualiza los fotogramas
    frame1 = frame2
    ret, frame2 = cap.read()

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(10) == ord('q'):
        break

# Libera la captura y cierra las ventanas
cap.release()
cv2.destroyAllWindows()