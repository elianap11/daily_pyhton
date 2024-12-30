'''
Para este proyecto, crearemos una aplicación web interactiva con Dash que visualice las 
cantidades de diferentes frutas, como manzanas, naranjas, plátanos, uvas y fresas. Los 
usuarios podrán seleccionar una fruta específica de un menú desplegable y la aplicación 
mostrará un gráfico de barras que muestra la cantidad de esa fruta.

Puede utilizar los siguientes datos:

data = {
'Fruit': ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Strawberries'],
'Amount': [4, 1, 2, 5, 3],
}

Resultado esperado
Cuando el usuario selecciona otra fruta (por ejemplo, uvas), el gráfico se actualiza 
representando la cantidad de la fruta elegida. 

A continuación, se muestra una estructura de programa para comenzar.

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Datos de muestra
data = {
'Fruit': ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Strawberries'],
'Amount': [4, 1, 2, 5, 3],
}

df = pd.DataFrame(data)

# Inicializar la aplicación Dash
app = ...

# Definir el diseño
app.layout = html.Div([
...
...
])

# Definir la devolución de llamada para actualizar el gráfico
@app.callback(
...
...
)
def update_graph(selected_fruit):
...
...

# Ejecutar la aplicación
if __name__ == '__main__':
app.run_server(debug=True)

Requisitos previos
Bibliotecas requeridas: dash, plotly, pandas
pip install dash plotly pandas

'''
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Datos de muestra
data = {
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Strawberries'],
    'Amount': [4, 1, 2, 5, 3],
}

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Definir el diseño
app.layout = html.Div([
    html.H1("Visualización de Cantidades de Frutas"),
    dcc.Dropdown(
        id='fruit-dropdown',
        options=[{'label': fruit, 'value': fruit} for fruit in df['Fruit']],
        value='Apples'  # Valor inicial
    ),
    dcc.Graph(id='bar-chart')
])

# Definir la devolución de llamada para actualizar el gráfico
@app.callback(
    Output('bar-chart', 'figure'),
    Input('fruit-dropdown', 'value')
)
def update_graph(selected_fruit):
    # Filtrar el DataFrame basado en la fruta seleccionada
    filtered_df = df[df['Fruit'] == selected_fruit]
    # Crear un gráfico de barras
    fig = px.bar(filtered_df, x='Fruit', y='Amount', title=f'Cantidad de {selected_fruit}')
    return fig

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)