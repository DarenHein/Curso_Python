'''
diccionario 2 ahora jugaremos con un quipo de funbotl inventado 

'''

equipo = {10 : "Luis" , 9 : "kevin" , 8 : "sebas" , 7 : "axel"}

# si al ingresar el numero al imprimir se ocupa lo diuguiente 

op  = int (input("que jugador deseas buscar ingresa su numero de camiseta ; "))

print(equipo.get(op,"No se enceuntra en la base de datos ")) # co esto la vvariable op guarda el numero si el numero concuerda con la llave del diccionario impimiria el dato correspondiente ala llave si no mnadara el mensaje que se encuntra entre comillas 

# imprimir solo llaves en patalla 
print(equipo.keys()) # con esto solo se imprimira las llaves correspondientes no los datos 

# imprimir solo los datos NO  las llves 
print(equipo.values()) 
# con esto solo imprimiremos los datos que perttecen als llaves NO LAS LLAVES 

# buscar solo unfatp 
print(10 in equipo) # devolvera un valor booleano dependiendo si esta o no 
op2 = 100 in equipo

if op2 == True : 
    print(" si esta en el equipo")
else : 
    print(" no esta en el equipo ")

print (equipo.items()) # los transforma atuplas 
print(len(equipo)) # nos marca cuantos elementos hay en el diccionario 

#borrar elemntos 

equipo.clear() # elimina todo de todo 
