'''
bucle while 
en python solo hay dos bucles repetitivos 

while 
for 

(por desgrac)a solo hay dos te extrañare do while jajajjaja

ya sabemos con python que en while primero piensa la condicion luego ejecuta 

un puequeño ejemplo aremos la raiz de un numero pero si el usuario ingresa la raiz de un negativo mandara un mensaje 
'''

import math

numero = int (input("ingresa un numero : "))

while numero<0 : 
    print("error ingresa otro numero ")
    numero = int (input("ingresa un numero : "))

print(f"la raiz cuadrada dle numero es {math.sqrt(numero)}")
