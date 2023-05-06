'''
los diccionarios son colecciones desordenadas preo estas se vasan en clave : infromacion 

ahora vamos a hacer un pequeño ejemplos de colores ingles español 
'''

diccionario = {"azul" : "blue" , "rojo" : "red" , "verde" : "green"}

print(diccionario) # asi se imprmen todos los datos de el diccionario 

print(diccionario["azul"]) # si solo queremos un dato en especifico tenemos que seleccionar la clave y en terminal se imprimira la infromacion 

# AGREGAR ELEMENTO 

diccionario["naranja"] = "Orange" # praa agregar clave y dato al diccionario 
print(diccionario)

# para eliminar un elemento del diccionario 
del(diccionario["naranja"]) # cindicamos la clave que deseamos eliminar y en automatico se elimina el dato 
print(diccionario)

'''
los diccionarios tambien pueden contener listas tuplas conjuntos y hasta otros diccionarios 
ahoriata un ejemplo 
'''
diccionario2 = {"Luis" : ["19","1.78" ] , "Kelly" : ["29","1.60"]} # diccionario con lista 
print(diccionario2) # al momento de imrpmir salda todo 

# diccionario con diccionario 
diccionario3 = {"Luis" : {"edad":30,"Peso":"80 kg "}}
print(diccionario3)