'''
Descripción del proyecto
Para este proyecto, crearemos una aplicación web utilizando el marco web FastHTML de Python.

Crearemos un sitio web de una sola página. En el sitio web, mostraremos un código Python 
(como se muestra arriba) con su sintaxis resaltada como corresponde y un botón para que los 
visitantes copien el código. Esta aplicación puede servir para compartir código con otras 
personas. Así es como se ve el resultado. Estamos mostrando un código Python aleatorio 
en este ejemplo. Vaya al botón "Mostrar código" para ver el código FastHTML que crea el 
siguiente sitio web.

Beneficios del aprendizaje
Este proyecto aprovecha el marco web FastHTML de Python, una herramienta poderosa para crear 
aplicaciones web rápidas, eficientes y escalables con una configuración mínima. FastHTML está 
diseñado específicamente para desarrolladores que desean crear aplicaciones web modernas 
utilizando solo Python, lo que elimina la necesidad de lenguajes adicionales o configuraciones 
complejas. Combina la facilidad de uso con el rendimiento necesario para manejar proyectos más 
grandes, lo que lo hace ideal tanto para principiantes como para desarrolladores experimentados 
que buscan mejorar sus habilidades en el desarrollo web.

Prerrequisitos
Bibliotecas requeridas: fasthtml
pip install python-fasthtml
'''

from fasthtml import FastHTML

# Crear la aplicación
app = FastHTML()

# Código Python a mostrar
python_code = """\
import folium
import pandas as pd

# Load the CSV file containing country names and coordinates
def load_data():
    return pd.read_csv("europe.csv")
data = load_data()

# Create a Folium map centered around Europe
m = folium.Map(location=[data["Latitude"].mean(), data["Longitude"].mean()], zoom_start=4)

# Add country names as labels to the map
for _, row in data.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=row["Country"],
        tooltip=row["Country"],
    ).add_to(m)

m.save("map.html")
"""

# Definir la ruta principal
@app.route("/", methods=["GET"])
def home():
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Folium Code Snippet</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                padding: 20px;
                background-color: #f4f4f4;
            }}
            pre {{
                background-color: #fff;
                border: 1px solid #ccc;
                padding: 10px;
                border-radius: 5px;
                overflow: auto;
                color: #333;
                white-space: pre-wrap; /* Permitir que haya un ajuste de línea */
                word-wrap: break-word; /* Romper palabras largas */
            }}
            button {{
                margin-top: 10px;
                padding: 10px 15px;
                cursor: pointer;
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 5px;
            }}
            button:hover {{
                background-color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <h1>Folium Code Snippet</h1>
        <p>Feel free to use the following code as you wish:</p>
        <pre id="code">{python_code}</pre>
        <button onclick="copyCode()">Copiar Código</button>
        <script>
            function copyCode() {{
                const code = document.getElementById('code').innerText;
                navigator.clipboard.writeText(code).then(() => {{
                    alert('Código copiado al portapapeles!');
                }});
            }}
        </script>
    </body>
    </html>
    """

# Ejecutar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
