'''
Escriba un programa que le permita buscar un elemento químico por su símbolo y obtener su nombre 
completo y número atómico. El programa utiliza un diccionario de elementos predefinido. Para ayudarte, 
puedes empezar colocando este diccionario encima del script:

elements = {
"H": {"name": "Hidrógeno", "atomic_number": 1},
"He": {"name": "Helio", "atomic_number": 2},
"Li": {"name": "Litio", "atomic_number": 3},
"Be": {"name": "Berilio", "atomic_number": 4},
"B": {"name": "Boro", "atomic_number": 5},
"C": {"name": "Carbono", "atomic_number": 6},
"N": {"name": "Nitrógeno", "atomic_number": 7},
"O": {"name": "Oxígeno", "atomic_number": 8},
"F": {"name": "Flúor", "atomic_number": 9},
"Ne": {"name": "Neón", "atomic_number": 10},
"Na": {"nombre": "Sodio", "número_atómico": 11},
"Mg": {"nombre": "Magnesio", "número_atómico": 12},
"Al": {"nombre": "Aluminio", "número_atómico": 13},
"Si": {"nombre": "Silicio", "número_atómico": 14},
"P": {"nombre": "Fósforo", "número_atómico": 15},
"S": {"nombre": "Azufre", "número_atómico": 16},
"Cl": {"nombre": "Cloro", "número_atómico": 17},
"Ar": {"nombre": "Argón", "número_atómico": 18},
"K": {"nombre": "Potasio", "número_atómico": 19},
"Ca": {"nombre": "Calcio", "número_atómico": 20},
"Sc": {"nombre": "Escandio", "número_atómico": 21},
"Ti": {"nombre": "Titanio", "número_atómico": 22},
"V": {"nombre": "Vanadio", "número_atómico": 23},
"Cr": {"nombre": "Cromo", "número_atómico": 24},
"Mn": {"nombre": "Manganeso", "número_atómico": 25},
"Fe": {"nombre": "Hierro", "número_atómico": 26},
"Co": {"nombre": "Cobalto", "número_atómico": 27},
"Ni": {"nombre": "Níquel", "número_atómico": 28},
"Cu": {"nombre": "Cobre", "número_atómico": 29},
"Zn": {"nombre": "Zinc", "número_atómico": 30}
}

El programa solicita al usuario que ingrese un símbolo de elemento (es decir, “O”). Luego, 
el programa devuelve la información sobre ese elemento (es decir, “Oxígeno: número atómico 8”).
'''

elements = {
    "H": {"name": "Hidrógeno", "atomic_number": 1},
    "He": {"name": "Helio", "atomic_number": 2},
    "Li": {"name": "Litio", "atomic_number": 3},
    "Be": {"name": "Berilio", "atomic_number": 4},
    "B": {"name": "Boro", "atomic_number": 5},
    "C": {"name": "Carbono", "atomic_number": 6},
    "N": {"name": "Nitrógeno", "atomic_number": 7},
    "O": {"name": "Oxígeno", "atomic_number": 8},
    "F": {"name": "Flúor", "atomic_number": 9},
    "Ne": {"name": "Neón", "atomic_number": 10},
    "Na": {"name": "Sodio", "atomic_number": 11},
    "Mg": {"name": "Magnesio", "atomic_number": 12},
    "Al": {"name": "Aluminio", "atomic_number": 13},
    "Si": {"name": "Silicio", "atomic_number": 14},
    "P": {"name": "Fósforo", "atomic_number": 15},
    "S": {"name": "Azufre", "atomic_number": 16},
    "Cl": {"name": "Cloro", "atomic_number": 17},
    "Ar": {"name": "Argón", "atomic_number": 18},
    "K": {"name": "Potasio", "atomic_number": 19},
    "Ca": {"name": "Calcio", "atomic_number": 20},
    "Sc": {"name": "Escandio", "atomic_number": 21},
    "Ti": {"name": "Titanio", "atomic_number": 22},
    "V": {"name": "Vanadio", "atomic_number": 23},
    "Cr": {"name": "Cromo", "atomic_number": 24},
    "Mn": {"name": "Manganeso", "atomic_number": 25},
    "Fe": {"name": "Hierro", "atomic_number": 26},
    "Co": {"name": "Cobalto", "atomic_number": 27},
    "Ni": {"name": "Níquel", "atomic_number": 28},
    "Cu": {"name": "Cobre", "atomic_number": 29},
    "Zn": {"name": "Zinc", "atomic_number": 30}
}

symbol = input("Ingresa el símbolo del elemento químico (ejemplo: O): ")

if symbol in elements:
    element = elements[symbol]
    print(f"{element['name']}: número atómico {element['atomic_number']}")
else:
    print("Símbolo no encontrado. Por favor, verifica el símbolo ingresado.")