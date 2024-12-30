'''
Tu tarea de hoy es escribir un código que invierta cualquier cadena. Hay dos formas 
diferentes de lograr esto, una usando un bucle for y otra usando la segmentación de 
cadenas. Si puedes, escribe ambas soluciones.

Cómo funciona el proyecto
Comienza tu script definiendo una oración como una cadena. Aquí tienes un ejemplo:
text = "Python is fun!"

'''
text = "Python is fun!"
text_reverse = ""

#se recorre cada caracter de text y se coloca al inicio de text_reverse
for word in text:
    text_reverse = word + text_reverse

print(text_reverse)
    

#toma todos los caracteres en sentido inverso
text_reverse = text[::-1]  
print(text_reverse)