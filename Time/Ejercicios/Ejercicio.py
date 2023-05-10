'''
tres numeros porteclado 
diga cual es el mayor 

'''
import time 

while True : 

    num = int(input("ingresa un numero -> "))
    num2 = int(input("ingresa otro numero -> "))
    num3 =int(input("ingresa otro numero ->"))

    if num > num2 and num > num3 : 
        print(f"el numero mayor es {num}")
    elif num2 > num and num2 > num3 : 
        print(f"el numero mayor es {num2}")
    elif num3 > num2 and num3 > num2 : 
        print(f"el numero mayor es : {num3}")
    else : 
        print(" todos los numero son iguales ")