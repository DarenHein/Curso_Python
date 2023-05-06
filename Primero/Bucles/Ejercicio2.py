#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

num = int(input("ingresa un numero para hacer la suma : "))
i = 0 
while num != 0 : 
    i += num
    num = int(input("ingresa un numero para hacer la suma : "))

print(f"la suma de los numeros es : {i}")
