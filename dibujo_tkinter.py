'''
Aplicación de dibujo con Tkinter

En este proyecto, creará una aplicación de dibujo básica que permite a los usuarios dibujar líneas y formas a mano alzada en un lienzo usando el mouse.
La aplicación tendrá la capacidad de cambiar colores y tamaños de pincel. Los usuarios también podrán limpiar el lienzo y guardar su dibujo como un archivo de imagen.
Esta es una excelente manera de practicar el trabajo con el widget de lienzo de Tkinter, el manejo de eventos del mouse y el uso de bibliotecas básicas de procesamiento de imágenes para guardar el lienzo como una imagen.

Requisitos previos
Bibliotecas requeridas: tkinter, pillow
pip install pillow
'''

import tkinter as tk
from tkinter import colorchooser
from tkinter import filedialog
from PIL import Image, ImageDraw

class DrawingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Basic Drawing App")

        self.canvas = tk.Canvas(master, bg="white", width=800, height=600)
        self.canvas.pack()

        self.brush_color = "black"
        self.brush_size = 3

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        self.setup_toolbar()

        # Create an empty image for saving
        self.image = Image.new("RGB", (800, 600), "white")
        self.draw = ImageDraw.Draw(self.image)

    def setup_toolbar(self):
        toolbar = tk.Frame(self.master)
        toolbar.pack()

        color_button = tk.Button(toolbar, text="Pick Color", command=self.choose_color)
        color_button.pack(side=tk.LEFT)

        size_label = tk.Label(toolbar, text="Brush Size:")
        size_label.pack(side=tk.LEFT)

        self.size_slider = tk.Scale(toolbar, from_=1, to=100, orient=tk.HORIZONTAL, command=self.update_brush_size)
        self.size_slider.set(self.brush_size)
        self.size_slider.pack(side=tk.LEFT)

        clear_button = tk.Button(toolbar, text="Clear", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT)

        save_button = tk.Button(toolbar, text="Save Drawing", command=self.save_drawing)
        save_button.pack(side=tk.LEFT)

        exit_button = tk.Button(toolbar, text="Exit", command=self.master.quit)
        exit_button.pack(side=tk.LEFT)

    def choose_color(self):
        color = colorchooser.askcolor()
        if color[1]:
            self.brush_color = color[1]

    def update_brush_size(self, size):
        self.brush_size = int(size)

    def paint(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x - self.brush_size, y - self.brush_size, x + self.brush_size, y + self.brush_size, fill=self.brush_color, outline=self.brush_color)
        
        # Draw on the image
        self.draw.ellipse((x - self.brush_size, y - self.brush_size, x + self.brush_size, y + self.brush_size), fill=self.brush_color, outline=self.brush_color)

    def reset(self, event):
        pass

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image.paste("white", [0, 0, self.image.size[0], self.image.size[1]])  # Clear the image

    def save_drawing(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if file_path:
            self.image.save(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()