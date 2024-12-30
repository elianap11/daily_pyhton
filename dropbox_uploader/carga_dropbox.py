'''
En este proyecto, aprenderá a automatizar el proceso de carga de archivos a Dropbox con Python. 
Al crear esta aplicación, obtendrá experiencia práctica con las API de almacenamiento en la nube 
y la automatización de la carga de archivos. El script se autenticará con Dropbox a través de un 
token de acceso, cargará un archivo desde su sistema local y lo almacenará en su cuenta de Dropbox.

Siguiente
En el proyecto de ayer, creamos un script de Python que carga archivos a una cuenta de Dropbox 
a través de la API de Dropbox. En el proyecto de hoy, ampliamos ese programa creando una aplicación 
web que cualquier usuario puede usar para cargar archivos a nuestra cuenta de Dropbox. Una aplicación 
de este tipo puede ser útil en muchos escenarios cuando desea recibir archivos de un determinado grupo 
de usuarios.

Resultado esperado
La aplicación web permite al usuario cargar un archivo. Una vez que el usuario carga un archivo y 
presiona el botón "Cargar", la aplicación se almacenará dentro de la carpeta "Aplicaciones" en su 
cuenta de Dropbox.
'''
from flask import Flask, request, render_template
import dropbox

app = Flask(__name__)

# Token de acceso de tu aplicación de Dropbox
ACCESS_TOKEN = 'tu_token_de_acceso'

# Inicializar Dropbox
dbx = dropbox.Dropbox(ACCESS_TOKEN)

@app.route('/')
def index():
    return render_template('uploader.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    # Cargar archivo a Dropbox
    dbx.files_upload(file.read(), f'/Aplicaciones/{file.filename}')
    
    return f"File '{file.filename}' uploaded successfully to Dropbox at '/Aplicaciones/{file.filename}'"

if __name__ == '__main__':
    app.run(debug=True)
