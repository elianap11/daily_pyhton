'''
Estimador de precios inmobiliarios

El programa estima el precio de una propiedad en función del tamaño de la casa (en pies cuadrados) 
y su ubicación (ciudad o suburbio).

Resultado esperado
El programa comienza solicitando al usuario que ingrese los pies cuadrados de la propiedad. A continuación, 
el programa solicita que ingrese "ciudad" o "suburbio". Si el usuario ingresa "ciudad", el programa debe 
usar un precio de 250 dólares por pie cuadrado. Si ingresa "suburbio", el programa debe usar un precio de 
150 dólares por pie cuadrado.Una vez que el usuario ingresa "ciudad" o "suburbio", el programa muestra un 
mensaje donde incluye el precio estimado para la propiedad dada.
'''


# Función para estimar el precio de la propiedad
def estimar_precio(pies_cuadrados, ubicacion):
    if ubicacion.lower() == "ciudad":
        precio_por_pie = 250  # Precio en ciudad
    elif ubicacion.lower() == "suburbio":
        precio_por_pie = 150  # Precio en suburbio
    else:
        return None  # Ubicación no válida

    return pies_cuadrados * precio_por_pie

# Función principal
def main():
    try:
        # Solicitar al usuario el tamaño de la propiedad
        pies_cuadrados = float(input("Ingrese los pies cuadrados de la propiedad: "))
        
        # Solicitar la ubicación
        ubicacion = input("Ingrese la ubicación (ciudad o suburbio): ")

        # Estimar el precio
        precio_estimado = estimar_precio(pies_cuadrados, ubicacion)

        if precio_estimado is not None:
            print(f"El precio estimado para la propiedad es: ${precio_estimado:,.2f}")
        else:
            print("Ubicación no válida. Por favor ingrese 'ciudad' o 'suburbio'.")
    
    except ValueError:
        print("Por favor, ingrese un número válido para los pies cuadrados.")

# Ejecutar el programa
if __name__ == "__main__":
    main()