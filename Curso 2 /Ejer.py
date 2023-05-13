'''
ejercicio que ingrese nombre y apellido pero si tiene un espacioio de mas lo quite
en amobos lados con strip 
'''

nombre =  input("ingresa tu nombre -> ")
apellido = input("ingresa tu apellido -> ")

nombre = nombre.strip()
apellido = apellido.strip()

nombre2 = nombre.istitle()
apellido2 = apellido.istitle()

if nombre2 == False and apellido2 == False : 
    nombre = nombre.title()
    apellido = apellido.title()
    print(f"bienvenido {nombre} {apellido}")
elif nombre2 == True and apellido2 == False : 
    print("apellido mal escrito ")
    apellido = apellido.title()
    print(f"modfificaciones hechas el nombre -> {nombre} apellido -> {apellido}")
elif nombre2 == False and apellido2 == True : 
    print(f"el nombre esta mal escrito")
    nombre = nombre.title()
    print(f"datos modificados nombre -> {nombre} apellido -> {apellido}")
else : 
    print("esta bien escrito")