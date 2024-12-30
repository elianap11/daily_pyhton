'''
Este proyecto monitoreará los cambios en un directorio específico y los mostrará en tiempo real 
utilizando una interfaz gráfica de usuario simple creada con Tkinter. Puede usar esto para rastrear
modificaciones como la creación, eliminación o modificación de archivos en cualquier carpeta. 
Esto podría ser útil para aplicaciones como monitorear archivos de registro o vigilar un directorio
durante el desarrollo.

Cómo funciona el proyecto
El programa monitorea un directorio especificado por el usuario en tiempo real. Siempre que se agrega, 
elimina o modifica un archivo en ​​el directorio, se muestra una entrada de registro en una interfaz gráfica 
de usuario de Tkinter. La interfaz gráfica de usuario proporciona un registro desplazable en tiempo real 
de todos los cambios de archivos, lo que facilita ver lo que está sucediendo en la carpeta monitoreada.

'''

import os
import time
import tkinter as tk
from tkinter import scrolledtext, messagebox
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MonitorHandler(FileSystemEventHandler):
    """Clase para manejar eventos de cambios en el sistema de archivos."""
    
    def __init__(self, log_text):
        self.log_text = log_text

    def on_created(self, event):
        """Evento para cuando se crea un archivo."""
        self.log_event(f'Creado: {event.src_path}')

    def on_deleted(self, event):
        """Evento para cuando se elimina un archivo."""
        self.log_event(f'Eliminado: {event.src_path}')
    
    def on_modified(self, event):
        """Evento para cuando se modifica un archivo."""
        self.log_event(f'Modificado: {event.src_path}')

    def log_event(self, event_message):
        """Agrega un mensaje al registro de eventos."""
        self.log_text.configure(state='normal')
        self.log_text.insert(tk.END, event_message + '\n')
        self.log_text.configure(state='disabled')
        self.log_text.see(tk.END)  # Desplazar hacia abajo

class FileMonitorApp:
    """Clase que encapsula la aplicación de monitoreo."""
    
    def __init__(self, master):
        self.master = master
        master.title("Monitoreo de Archivos")

        self.label = tk.Label(master, text="Ingresa el directorio a monitorear:")
        self.label.pack()

        self.dir_entry = tk.Entry(master, width=50)
        self.dir_entry.pack()

        self.start_button = tk.Button(master, text="Comenzar a Monitorear", command=self.start_monitoring)
        self.start_button.pack()

        self.log_text = scrolledtext.ScrolledText(master, width=60, height=20, state='disabled')
        self.log_text.pack()

        self.observer = None

    def start_monitoring(self):
        """Inicia el monitoreo del directorio ingresado."""
        directory = self.dir_entry.get()
        if not os.path.isdir(directory):
            messagebox.showerror("Error", "El directorio no es válido.")
            return
        
        if self.observer:
            self.observer.stop()
            self.observer.join()

        self.log_text.configure(state='normal')
        self.log_text.delete(1.0, tk.END)
        self.log_text.configure(state='disabled')

        self.event_handler = MonitorHandler(self.log_text)
        self.observer = Observer()
        self.observer.schedule(self.event_handler, directory, recursive=True)
        self.observer.start()
        
        self.log_event("Monitoreando cambios en: " + directory)

    def log_event(self, event_message):
        """Agrega un mensaje al registro."""
        self.log_text.configure(state='normal')
        self.log_text.insert(tk.END, event_message + '\n')
        self.log_text.configure(state='disabled')
        self.log_text.see(tk.END)  # Desplazar hacia abajo

# Función principal para ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    file_monitor_app = FileMonitorApp(root)
    root.mainloop()