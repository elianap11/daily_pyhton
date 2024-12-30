'''
Cree un programa que comience con una lista predefinida de sus películas favoritas. Por ejemplo:

favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]
Coloque la lista anterior en su script.py y luego agregue un código que haga lo siguiente:

Agrega una nueva película a la lista (por ejemplo, "El Padrino").
Elimina una película específica de la lista (por ejemplo, "The Matrix").
Imprime la cantidad total de películas en la lista.
Imprime las películas en orden alfabético.
'''

# Lista predefinida de películas favoritas
favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]

# Agregar una nueva película
favorite_movies.append("El Padrino")

# Eliminar una película específica
favorite_movies.remove("The Matrix")

# Imprimir la cantidad total de películas en la lista
print("Cantidad total de películas:", len(favorite_movies))

# Imprimir las películas en orden alfabético
print("Películas en orden alfabético:", sorted(favorite_movies))