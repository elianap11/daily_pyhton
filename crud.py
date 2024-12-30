'''
Desarrolle una aplicación de línea de comandos que permita a una pequeña empresa administrar 
su inventario. La aplicación permitirá a los usuarios:
- agregar un artículo nuevo
- actualizar el stock
- ver todos los artículos
- buscar artículos específicos por nombre
'''
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in self.items:
            print(f"El artículo '{name}' ya existe. Use la opción de actualizar para cambiar el stock.")
        else:
            self.items[name] = quantity
            print(f"Artículo '{name}' agregado con una cantidad de {quantity}.")

    def update_stock(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
            print(f"Stock de '{name}' actualizado. Cantidad actual: {self.items[name]}.")
        else:
            print(f"El artículo '{name}' no existe. Agregue el artículo primero.")

    def view_all_items(self):
        if not self.items:
            print("No hay artículos en el inventario.")
        else:
            print("Artículos en el inventario:")
            for name, quantity in self.items.items():
                print(f" - {name}: {quantity}")

    def search_item(self, name):
        if name in self.items:
            print(f"Artículo encontrado: {name} - Cantidad: {self.items[name]}")
        else:
            print(f"El artículo '{name}' no se encuentra en el inventario.")


def main():
    inventory = Inventory()

    while True:
        print("\nOpciones:")
        print("1. Agregar un artículo nuevo")
        print("2. Actualizar stock")
        print("3. Ver todos los artículos")
        print("4. Buscar un artículo específico por nombre")
        print("5. Salir")

        choice = input("Seleccione una opción (1-5): ")

        if choice == '1':
            name = input("Ingrese el nombre del artículo: ")
            quantity = int(input("Ingrese la cantidad: "))
            inventory.add_item(name, quantity)
        elif choice == '2':
            name = input("Ingrese el nombre del artículo: ")
            quantity = int(input("Ingrese la cantidad a agregar: "))
            inventory.update_stock(name, quantity)
        elif choice == '3':
            inventory.view_all_items()
        elif choice == '4':
            name = input("Ingrese el nombre del artículo a buscar: ")
            inventory.search_item(name)
        elif choice == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()