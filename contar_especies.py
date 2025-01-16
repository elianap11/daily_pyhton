'''
Debe crear un programa que tome una lista de especies de árboles que se encuentran
 en un bosque y cuente cuántas veces aparece cada especie.
árboles = ["roble", "pino", "arce", "roble", "abedul", "pino", "roble"]
'''

# Lista de especies de árboles
trees = ["oak", "pine", "maple", "oak", "birch", "pine", "oak"]

# Crear un diccionario para contar cada especie
tree_count = {}

# Contar las especies
for tree in trees:
    if tree in tree_count:
        tree_count[tree] += 1
    else:
        tree_count[tree] = 1

# Imprimir el resultado
for tree, count in tree_count.items():
    print(f"{tree}: {count}")