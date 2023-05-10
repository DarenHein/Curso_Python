'''
aqui veremos los 3 metodos 

1 - strip() - elimina caracteres indicados solo del principio y final de la cadena si no se indica solo elimina espacios o saltos de linea 

'''

# ejemplo strip 
cadena = " hola " # tenemos una cadena 
cadena2 = cadena.strip() #almacenamos el strip en otra variable 
cadena3 = len(cadena2) # almacemanos ese mimos metodo en otra variable para contar los caracteres 
print(cadena3)# imprimimos para verificar 

#ejemplo 2 

cadena = "Hola Luis" # vamos a quitar la H de Hola por que solo puede quitar la priemera y ultima letra de la cadena 
cadena2 = cadena.strip("H") #indidcamos la letra que deseamos quitar 
print(cadena2)

