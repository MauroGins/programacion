#Diseñar un algoritmo que calcule y muestre en pantalla el factorial de un número entero dado.

    
import math

print("Introduce el numero del cual quieres conocer el factorial")
n = int(input())

result = math.factorial(n)

print(f"El factorial de {n} es {result}")