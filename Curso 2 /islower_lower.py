'''
los metodos lower y islower 

sirven para trasnfromar en minusculas como el title y is title 

islower -> verifica si hay una mayuscula en la cadena si hay devolvera un booleano 
lower -> trasmfromar la primera letra de la cadena en minuscla 

'''

cadena = input("Ingresa una cadena -z ")
cadena = cadena.strip()
cadena2 = cadena.islower()
print(cadena2)
if cadena2 == False :
    cadena = cadena.lower()
    print(cadena)
else : 
    print("el nombre este en minusculas :) ")