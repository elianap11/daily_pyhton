'''
Este programa define tres números y determina cuál es el mayor. Luego muestra el número más grande.
'''

num1 = 12
num2 = 45
num3 = 32

if num1 > num2 and num1 > num3:
    largest = num1
elif num2 > num1 and num2 > num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is {largest}")