'''
Cree una aplicación de línea de comandos de Python que obtenga los tipos de cambio 
de divisas en tiempo real y muestre los tipos de conversión entre una divisa base 
(como el dólar estadounidense) y una lista de divisas de destino seleccionadas por 
el usuario. La aplicación también permitirá a los usuarios convertir cantidades entre 
divisas y guardar los resultados en un archivo para consultarlos más adelante.

El usuario introduce el dólar estadounidense como divisa base y el euro como divisa de 
destino y envía un importe de 10 dólares estadounidenses y el programa devuelve 9,6 euros. 
El evento de cambio se guarda en un archivo de texto.

Sugerencia: puede utilizar la API de tipos de cambio de forma gratuita para obtener tipos 
de cambio en tiempo real con Python. No necesita una clave API.
'''
import requests

def obtener_tipos_de_cambio(base):
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        return respuesta.json()["rates"]
    else:
        print("Error al obtener los tipos de cambio.")
        return None

def convertir_divisas(cantidad, tipo_cambio):
    return cantidad * tipo_cambio

def guardar_resultado(base, destino, cantidad, resultado):
    with open("conversiones.txt", "a") as archivo:
        archivo.write(f"{cantidad} {base} = {resultado:.2f} {destino}\n")

def main():
    divisa_base = "USD"
    divisa_destino = input("Introduce la divisa de destino (por ejemplo, EUR): ").upper()
    cantidad = float(input(f"Introduce la cantidad en {divisa_base} que quieres convertir: "))
    
    tipos_de_cambio = obtener_tipos_de_cambio(divisa_base)
    if tipos_de_cambio and divisa_destino in tipos_de_cambio:
        tipo_cambio = tipos_de_cambio[divisa_destino]
        resultado = convertir_divisas(cantidad, tipo_cambio)
        print(f"{cantidad} {divisa_base} = {resultado:.2f} {divisa_destino}")
        
        guardar_resultado(divisa_base, divisa_destino, cantidad, resultado)
        print("Resultado guardado en 'conversiones.txt'.")
    else:
        print(f"No se encontró la divisa {divisa_destino}.")

if __name__ == "__main__":
    main()