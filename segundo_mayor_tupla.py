'''
Descripción del proyecto
Comenzaremos esta semana con un pequeño proyecto sobre tuplas. Tu tarea es escribir un 
programa que tome una tupla de números, encuentre el segundo número más grande e imprima 
ese número.

Puedes comenzar tu programa con esta tupla como primera línea:
numbers = (10, 5, 8, 20, 15)
'''

numbers = (10, 5, 8, 20, 15)
numbers = list(numbers)
numbers.sort()
print(numbers[-2])

