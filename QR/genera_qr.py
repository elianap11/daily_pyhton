'''
Esta aplicación Flask permitirá a los usuarios ingresar una URL y luego generará un código QR 
que pueden descargar como imagen. Cualquier persona que escanee el código QR generado será 
dirigida a la URL asociada con el código QR generado.

Resultado esperado
El usuario puede ingresar una URL y presionar el botón "Generar código QR"
Una vez que el usuario presiona el botón, se descarga una imagen PNG del código QR
El usuario puede escanear el código con la cámara de su teléfono móvil y el navegador 
debería abrir la página vinculada al código QR
'''

from flask import Flask, render_template, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    url = request.form['url']
    
    # Generar el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Guardar la imagen en un buffer
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    # Enviar la imagen como archivo para descargar
    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='codigo_qr.png')

if __name__ == '__main__':
    app.run(debug=True)