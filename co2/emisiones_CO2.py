'''
Este programa de Python analizará un conjunto de datos que contiene los niveles de emisión de CO2
a lo largo de los años. El programa permitirá a los usuarios visualizar las tendencias de las 
emisiones de CO2, identificar patrones estacionales y calcular estadísticas básicas (como niveles 
promedio, máximo y mínimo). Ayudará a los usuarios a comprender el impacto de la actividad humana 
en el medio ambiente al visualizar los cambios en la concentración de CO2 a lo largo del tiempo.

Usaremos pandas para la manipulación de datos, matplotlib para representar gráficamente los datos
y seaborn para funciones de visualización de datos adicionales. Para esto, podemos usar datos 
disponibles públicamente, como los niveles de CO2 del Observatorio de Mauna Loa de donde descargamos
co2.csv. El programa debería generar el siguiente gráfico a partir del archivo CSV vinculado 
anteriormente. Muestra la cantidad de CO2 en ppm durante los últimos cuatro años.

'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos desde el archivo CSV
co2_data = pd.read_csv('co2.csv')

# Imprimir las columnas del DataFrame para verificar
print("Columnas en el DataFrame:", co2_data.columns)

# Crear una columna de fecha a partir de Year y Month
co2_data['Date'] = pd.to_datetime(co2_data['Year'].astype(str) + '-' + co2_data['Month'].astype(str) + '-01')

# Filtrar los datos para los últimos cuatro años
last_four_years = co2_data[co2_data['Date'] >= pd.Timestamp.now() - pd.DateOffset(years=4)]

# Calcular estadísticas
average_co2 = last_four_years['CO2_Level'].mean()
max_co2 = last_four_years['CO2_Level'].max()
min_co2 = last_four_years['CO2_Level'].min()

print(f"Promedio de CO2 (ppm) en los últimos cuatro años: {average_co2:.2f}")
print(f"Máximo de CO2 (ppm) en los últimos cuatro años: {max_co2:.2f}")
print(f"Mínimo de CO2 (ppm) en los últimos cuatro años: {min_co2:.2f}")

# Visualización
plt.figure(figsize=(12, 6))
sns.lineplot(data=last_four_years, x='Date', y='CO2_Level', marker='o')
plt.title('Niveles de CO2 en los últimos cuatro años')
plt.xlabel('Año')
plt.ylabel('Niveles de CO2 (ppm)')
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()