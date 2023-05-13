'''
metodos istitle y title

istitle -> devuvlve un true o false si la primera letra dela cadena selecciona es minuscula 

true -> primera letra mayuscula 
false -> no es mayuscula 

title -> transfoma la primera letra en mayuscula y lo demas en minusculas 

se puede ocupar con if para mayor eficacia 
'''

cadena = "luis"
cadena = cadena.istitle()
print(cadena)

# ejemplo 2 

cadena2 = "holamundo"
cadena2 = cadena2.title()
print(cadena2)

# ejemplo 3 

cadena3 = "kelly"
cadena4 = cadena3.istitle()
if cadena4 == False : 
    cadena3 = cadena3.title()
    print(cadena3)
else : 
    print("esta correctamente escrito tu nombre ")