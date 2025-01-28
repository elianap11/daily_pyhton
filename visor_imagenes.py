'''
En este proyecto, crearemos un visor de galería de imágenes simple donde los usuarios podrán 
explorar las imágenes almacenadas en una carpeta. La aplicación permitirá al usuario seleccionar 
una carpeta de su computadora y mostrar las imágenes de esa carpeta.

Este proyecto es útil para crear una aplicación GUI utilizando una de las mejores bibliotecas GUI
como PyQt6, y presenta a los usuarios la administración de sistemas de archivos, el trabajo con 
imágenes y el manejo de eventos GUI.

'''

import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class VisorImagenes(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visor de Imágenes")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.image_label = QLabel("Selecciona una carpeta para ver las imágenes")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.image_label)

        self.load_button = QPushButton("Cargar Carpeta")
        self.load_button.clicked.connect(self.load_folder)
        self.layout.addWidget(self.load_button)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        
        self.images = []  # Lista para almacenar las rutas de las imágenes
        self.current_image_index = -1

    def load_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Seleccione una Carpeta")
        if folder:
            self.images = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
            self.current_image_index = 0
            self.show_image()

    def show_image(self):
        if self.images:
            pixmap = QPixmap(self.images[self.current_image_index])
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.AspectRatioMode.KeepAspectRatio))

def main():
    app = QApplication(sys.argv)
    window = VisorImagenes()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()