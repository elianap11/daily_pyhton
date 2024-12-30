'''
Realizar una categorización de los datos del diccionario que contiene las 
calificaciones de los estudiantes.

grades = {
"Alice": 78,
"Bob": 42,
"Charlie": 65,
"Diana": 49,
"Eve": 90
}

El código debería crear un nuevo diccionario que clasifique a los estudiantes en 
"Aprobado" o "Reprobado" según sus calificaciones. Considere una calificación de 50 
0o más como "Aprobado" y una calificación inferior a 50 como "Reprobado". Una vez 
que cree un diccionario, use un bucle for para iterar sobre el nuevo diccionario 
e imprimir cada par de clave y valor.
'''

grades = {
"Alice": 78,
"Bob": 42,
"Charlie": 65,
"Diana": 49,
"Eve": 90
}

new_dict = {}

for key, value in grades.items():
    if value >= 50:
        new_dict[key] = "Aprobado"
    else:
        new_dict[key] = "Reprobado"

for key, value in new_dict.items():
    print(f"{key}: {value}")
    