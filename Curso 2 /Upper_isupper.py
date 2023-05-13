'''
upper y isupper es lo contrario a lower y islower 

este metodo vuelve mayusculas todas las palabras de la cadena 

isupper -> devuelve un true o false 
upper -> transforma las letras en mayusculas 

'''

cadena = input("ingresa una palabra o cadena -> ")
cadena.strip()
cadena2 = cadena.isupper()
print(cadena2)
if cadena2 == False :
    cadena3 = cadena.upper()
    print(cadena3)
else : 
    print("palara escrita correctamente  :) ")