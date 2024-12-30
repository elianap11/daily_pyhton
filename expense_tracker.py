'''
Crea una aplicación de línea de comandos para realizar un seguimiento de los gastos diarios. 
La aplicación permite a los usuarios agregar gastos, ver un resumen de todos los gastos y 
calcular el gasto total para un período determinado. 

Esto es lo que hace la aplicación:
Agregar gasto: ingresa la fecha, la categoría, la descripción y el monto.
Ver todos los gastos: muestra todos los gastos registrados en un formato tabular ordenado
Buscar gastos por fecha: ve los gastos para una fecha específica o un rango de fechas.
Calcular el gasto total: muestra el monto total gastado en todas las categorías
Guardar y cargar datos: guarda los registros de gastos en un archivo y cárgalos al iniciar la 
aplicación.
'''

import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, date, category, description, amount):
        expense = {
            'date': date,
            'category': category,
            'description': description,
            'amount': float(amount)
        }
        self.expenses.append(expense)
        print("Gasto agregado correctamente.")

    def view_expenses(self):
        if not self.expenses:
            print("No hay gastos registrados.")
            return

        print(f"{'Fecha':<12} {'Categoría':<15} {'Descripción':<30} {'Monto':<10}")
        print("=" * 70)
        for expense in self.expenses:
            print(f"{expense['date']:<12} {expense['category']:<15} {expense['description']:<30} {expense['amount']:<10.2f}")

    def search_expenses_by_date(self, start_date, end_date):
        filtered_expenses = [e for e in self.expenses if start_date <= e['date'] <= end_date]
        
        if not filtered_expenses:
            print(f"No se encontraron gastos entre {start_date} y {end_date}.")
            return
        
        print(f"{'Fecha':<12} {'Categoría':<15} {'Descripción':<30} {'Monto':<10}")
        print("=" * 70)
        for expense in filtered_expenses:
            print(f"{expense['date']:<12} {expense['category']:<15} {expense['description']:<30} {expense['amount']:<10.2f}")

    def calculate_total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"Gasto total: {total:.2f}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n1. Agregar gasto")
        print("2. Ver todos los gastos")
        print("3. Buscar gastos por fecha")
        print("4. Calcular gasto total")
        print("5. Salir")
        choice = input("Selecciona una opción: ")

        if choice == '1':
            date = input("Ingresa la fecha (YYYY-MM-DD): ")
            category = input("Ingresa la categoría: ")
            description = input("Ingresa la descripción: ")
            amount = input("Ingresa el monto: ")
            tracker.add_expense(date, category, description, amount)

        elif choice == '2':
            tracker.view_expenses()

        elif choice == '3':
            start_date = input("Ingresa la fecha de inicio (YYYY-MM-DD): ")
            end_date = input("Ingresa la fecha de fin (YYYY-MM-DD): ")
            tracker.search_expenses_by_date(start_date, end_date)

        elif choice == '4':
            tracker.calculate_total_expenses()

        elif choice == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    main()

