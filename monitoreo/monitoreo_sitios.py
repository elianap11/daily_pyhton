''' 
Crea una herramienta de línea de comandos que monitoree el estado de una lista de sitios web. La aplicación lee un archivo website.txt donde has enumerado los sitios web que quieres revisar. Por ejemplo:

Contenido de website.txt:

https://www.google.com
https://www.github.com
https://www.nonexistentwebsite12345.com
https://www.wikipedia.org
Cuando se ejecuta, el programa imprime el estado de cada sitio web:

Opcionalmente, el programa registra el tiempo de respuesta y el código de estado HTTP y envía los resultados a un archivo log.csv. Así es como debería verse el archivo log.csv generado después de ejecutar el programa:

Timestamp,URL,Response Time (ms),Status Code,Status
2024-12-12 16:19:59,https://www.google.com,413.866,200,Online
2024-12-12 16:20:00,https://www.github.com,191.506,200,Online
2024-12-12 16:20:00,https://www.nonexistentwebsite12345.com,N/A,N/A,Offline
2024-12-12 16:20:00,https://www.wikipedia.org,181.905,200,Online
'''

import requests
import csv
from datetime import datetime

# Read website URLs from the file
with open('./monitoreo/website.txt', 'r') as f:
    website_urls = [url.strip() for url in f.readlines()]

# Open the log file in write mode
with open('log.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Timestamp', 'URL', 'Response Time (ms)', 'Status Code', 'Status'])

    # Monitor each website
    for url in website_urls:
        try:
            # Send a GET request to the URL
            start_time = datetime.now()
            response = requests.get(url)
            end_time = datetime.now()
            response_time_ms = (end_time - start_time).total_seconds() * 1000

            # Check the status code
            if response.status_code == 200:
                status = 'Online'
            else:
                status = 'Offline'

            # Write the results to the log file
            writer.writerow([start_time.strftime('%Y-%m-%d %H:%M:%S'), url, response_time_ms, response.status_code, status])
            print(f"{start_time.strftime('%Y-%m-%d %H:%M:%S')} | {url} | {response_time_ms:.3f} ms | {response.status_code} | {status}")

        except requests.exceptions.RequestException:
            # Handle exceptions (e.g., network errors, non-existent websites)
            start_time = datetime.now()
            writer.writerow([start_time.strftime('%Y-%m-%d %H:%M:%S'), url, 'N/A', 'N/A', 'Offline'])
            print(f"{start_time.strftime('%Y-%m-%d %H:%M:%S')} | {url} | N/A | N/A | Offline")