# pedir 3 numeros por teclado y que el programa diga cual es el mas grande 

num = int (input("ingresa un numero -> "))
num2 = int (input("ingresa un numero -> "))
num3 = int (input("ingresa un numero -> "))

if num > num2 and num > num3 : 
    print(f"el numero {num} es el mayor")
elif num2 > num and num > num3 : 
    print(f"el numero {num2} es el mayor")
elif num3 > num and num > num2 :
    print(f"el numero mayor es num3")
else :
    print("los 3 numeros son iguales ")