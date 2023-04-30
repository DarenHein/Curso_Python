# ejercicio condicionales 

'''
dos numeros entrda por teclado y diga si son pares o inpares 


'''

num = int (input("ingresa un numero : "))
num2 = int (input("ingresa el otro numero : "))

# ahora si se viene lo bueno vamos a alocarnos 


if num % 2 == 0 and num2 % 2 > 0: # si entra aqui cumple que num es par pero num2 no 
    print (f"el nuemro { num } es par y {num2 } es inpar  ")
elif num % 2 > 0 and num2 % 2 ==0 : # si entra aqui num no es par pero num2 si lo es 
    print (f" el numero { num2 } es par {num  } es inpar ")
elif num % 2 == 0 and num2 % 2 ==0 : # si entra aqui ambos numeros son pares 
    print (f"cmo { num } y { num2 } son numero pares ")
else : 
    print (" ambos numeros son inpares ") # si entra aqui ambos numeros son inpares 