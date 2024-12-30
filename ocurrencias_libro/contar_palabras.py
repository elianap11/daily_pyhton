'''
Cree un programa Python para contar las ocurrencias de cualquier palabra dada en el libro 
almacenado en un archivo de texto. El usuario puede ingresar cualquier palabra (por ejemplo, 
nieve) y el programa debería averiguar cuántas ocurrencias de esa palabra existen en el archivo
book.txt e imprimir un mensaje: La palabra "nieve" aparece 103 veces en el archivo "book.txt".

Beneficios del aprendizaje
Manejo de archivos: aprenda a abrir, leer y cerrar archivos de texto.
Manipulación de cadenas: practique el trabajo con cadenas y métodos de cadenas como split(), count(), etc.
Entrada y salida: aprenda a tomar la entrada del usuario y mostrar la salida en la consola.
'''

# Función para contar las ocurrencias de una palabra en un archivo
def contar_ocurrencias(palabra):
    try:
        # Abrir el archivo en modo lectura
        with open(".//dia41//book.txt", 'r', encoding='utf-8') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()
            # Contar las ocurrencias de la palabra (sin distinguir entre mayúsculas y minúsculas)
            contador = contenido.lower().count(palabra.lower())
            return contador
    except FileNotFoundError:
        print("El archivo 'book.txt' no se encontró.")
        return 0

# Solicitar al usuario que ingrese la palabra que desea contar
palabra_buscada = input("Ingrese la palabra que desea contar: ")

# Contar las ocurrencias de la palabra en el archivo
ocurrencias = contar_ocurrencias(palabra_buscada)

# Imprimir el resultado
print(f'La palabra "{palabra_buscada}" aparece {ocurrencias} veces en el archivo "book.txt".')