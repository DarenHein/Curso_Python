#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

num = int(input("ingresa un numero : "))
num2 = int(input("ingresa otro numero para compara : "))

while num != 0 : 
    if num > num2 : 
        print(f"el numero mayor {num}")
    else : 
        print(f" el numero mayor es {num2} ")
    num = int(input("ingresa un numero : "))
    num2 = int(input("ingresa otro numero para compara : "))
