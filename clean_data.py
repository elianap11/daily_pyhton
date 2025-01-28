'''
Para este proyecto, se le proporciona la siguiente lista desordenada de cadenas que 
representan nombres:
messy_names = [" alice ", "Bob", " charlie", "Alice", "BOB ", "eve ", " Eve", "eve"]
Como puedes ver, algunos nombres están en minúsculas, algunos tienen espacios adicionales
 y otros son duplicados. Escribe un programa que limpie los datos eliminando los espacios 
 adicionales, convirtiendo todos los nombres a mayúsculas y minúsculas y eliminando los 
 duplicados. Por último, muestra la lista limpia en orden alfabético. Tu tarea es escribir 
 un programa que limpie los datos eliminando los espacios adicionales, convirtiendo todos 
 los nombres a mayúsculas y minúsculas (por ejemplo, Alice) y eliminando los duplicados. 
 Por último, muestra la lista limpia en orden alfabético.
'''

messy_names = [" alice ", "Bob", " charlie", "Alice", "BOB ", "eve ", " Eve", "eve"]

# conjunto para eliminar duplicados automáticamente
cleaned_names = set() 

for name in messy_names:
    # Eliminar espacios
    cleaned_name = name.strip().capitalize()
    cleaned_names.add(cleaned_name)

# Convertir el conjunto a una lista y ordenarla alfabéticamente
sorted_names = sorted(cleaned_names)

print(sorted_names)
