'''
Escriba un programa que tome una lista de palabras y encuentre la que aparece 
con más frecuencia. Comience escribiendo esta lista en la primera línea de su 
programa:

words = ["love", "peace", "joy", "love", "happiness", "love", "joy"]

Su programa debería encontrar la palabra más frecuente e imprimir un mensaje 
similar al siguiente donde se menciona la palabra más frecuente (es decir, "love").

'''

words = ["love", "peace", "joy", "love", "happiness", "love", "joy"]

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

most_frequent_word = max(frequency, key=frequency.get)
most_frequent_count = frequency[most_frequent_word]

print(f"La palabra que aparece con más frecuencia es '{most_frequent_word}' con {most_frequent_count} ocurrencias.")