'''
Crear un sistema de préstamo de libros basado en consola para una biblioteca pequeña o una colección personal de libros. 
Permite a los usuarios buscar libros disponibles, pedir prestado un libro, devolverlo y ver todos los libros prestados.
El usuario puede elegir la opción 1 para ver los libros disponibles para pedir prestado:
El usuario puede elegir la opción 2 y luego ingresar el número del libro que desea pedir prestado:
El usuario puede elegir la opción 3 para devolver un libro de modo que vuelva a estar disponible para pedir prestado:
👉 Te desafiamos a que uses clases (es decir, programación orientada a objetos) en lugar de funciones esta vez. 
Así es como se vería el código. Puedes completar el resto tú mismo.

clase BookLendingSystem:
def __init__(self):
self.libros_disponibles = {
1: "El gran Gatsby",
2: "Matar a un ruiseñor",
3: "1984",
4: "Orgullo y prejuicio"
}
self.libros_prestados = {}

def display_menu(self):
print("\n¡Bienvenido al sistema de préstamo de libros!")
...
...

def view_available_books(self):
...
...

def borrow_book(self):
if not self.available_books:
...
...

def return_book(self):
if not self.borrowed_books:
...
...

def view_borrowed_books(self):
if not self.borrowed_books:
...
...

def run(self):
while True:
self.display_menu()
choice = input("\nElija una opción: ").strip()
if choice == "1":
...
...

system = BookLendingSystem()
system.run()

Beneficios del aprendizaje
Practicará la gestión de listas y diccionarios, el manejo de la entrada del usuario y la implementación de flujos de trabajo lógicos para una aplicación interactiva. Además, practicará el trabajo con clases.

Requisitos previos
Bibliotecas requeridas: No se necesitan bibliotecas para este proyecto.
Archivos requeridos: No se necesitan archivos para este proyecto.
IDE: Puede usar cualquier IDE en su computadora para codificar el proyecto.
'''

class BookLendingSystem:
    def __init__(self):
        self.libros_disponibles = {
            1: "El gran Gatsby",
            2: "Matar a un ruiseñor",
            3: "1984",
            4: "Orgullo y prejuicio"
        }
        self.libros_prestados = {}

    def display_menu(self):
        print("\n¡Bienvenido al sistema de préstamo de libros!")
        print("1. Ver libros disponibles")
        print("2. Pedir prestado un libro")
        print("3. Devolver un libro")
        print("4. Ver libros prestados")
        print("5. Salir")

    def view_available_books(self):
        if not self.libros_disponibles:
            print("No hay libros disponibles en este momento.")
        else:
            print("Libros disponibles para pedir prestado:")
            for num, title in self.libros_disponibles.items():
                print(f"{num}. {title}")

    def borrow_book(self):
        self.view_available_books()
        if not self.libros_disponibles:
            return

        try:
            choice = int(input("Ingrese el número del libro que desea pedir prestado: "))
            if choice in self.libros_disponibles:
                self.libros_prestados[choice] = self.libros_disponibles.pop(choice)
                print(f"Has pedido prestado '{self.libros_prestados[choice]}'.")
            else:
                print("Número de libro no válido, intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    def return_book(self):
        if not self.libros_prestados:
            print("No has pedido prestado ningún libro.")
            return

        print("Libros prestados:")
        for num, title in self.libros_prestados.items():
            print(f"{num}. {title}")

        try:
            choice = int(input("Ingrese el número del libro que desea devolver: "))
            if choice in self.libros_prestados:
                self.libros_disponibles[choice] = self.libros_prestados.pop(choice)
                print(f"Has devuelto '{title}'. Gracias.")
            else:
                print("Número de libro no válido, intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    def view_borrowed_books(self):
        if not self.libros_prestados:
            print("No has pedido prestado ningún libro.")
        else:
            print("Libros prestados:")
            for num, title in self.libros_prestados.items():
                print(f"{num}. {title}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nElija una opción: ").strip()
            if choice == "1":
                self.view_available_books()
            elif choice == "2":
                self.borrow_book()
            elif choice == "3":
                self.return_book()
            elif choice == "4":
                self.view_borrowed_books()
            elif choice == "5":
                print("Gracias por usar el sistema de préstamo de libros. ¡Hasta luego!")
                break
            else:
                print("Opción no válida, intente nuevamente.")


# Crear una instancia del sistema y ejecutarlo
system = BookLendingSystem()
system.run()