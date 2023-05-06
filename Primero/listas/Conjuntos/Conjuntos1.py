# los conjuntos son otro tipo de colleciones estos a diferencia de las tuplas y listas es que estos NO PUEDEN CONTENER OTRO TIPO DE COLLECIONES DENTRO DE ELLA Y TAMPOCO REPETIDOS 

# los conjunto son una coleccion de elementos desordenados  

# conjuntos 

conjunto = set() # hay otro tipo de colleciones llamdas diccionarios pory oucpan el mismo simbolo que son los {}

conjunto = {"hola",1,2,3,4,5,6} # pueden almacenar datos reperidos y string y enteeros  pero NO  otro tipo de collecioens 

print(conjunto) 

# OTRO DATO IMPORTANTE ES QUE SE IMPRIMER AL REVES 

#agregar elementos a los conjuntos 
conjunto.add("Kevin es puto") # al momento de imprimir en pantalla todos saldran desordenados 

#eliminar elementos de los conjuntos 
conjunto.discard("Kevin es puto")# elimina un elemneto en especifico 
conjunto.clear()# borra todos los elemntos del conjunto 

#buscar elementos en el conjunto 
print(1 in conjunto) # devuvelve un booleano 
print(1 not in conjunto) # tambien se puede 