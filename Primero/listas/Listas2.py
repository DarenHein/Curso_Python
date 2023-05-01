#listas 2 algunos metodos 
# me recuerdan a los arry list o crud de java 

lista = [1,2,3,4,5,"Luis","Luis"]

#METODOS 

print(len(lista)) # saber cuantos elementos hay en la lista 


# agregar eñementos als lista 
lista.append(6) # agrega elemento al final de la lista 
lista.insert(2,0) # agrega un elemnto en un forma especifica el primer parametro ubica el lugar y el segundo que se agregara 
lista.extend([2,3,4]) #concatena esta nueva lista ala lista indicada 

# Sumar dos listas 

lista2 = ["kellys"]
lista3 = lista + lista2 
print(lista3)

#Buscar elemento en la lista 

print(3 in lista) # el 3 el elemto que deseamos buscar in = en lista es el nombre de la lista valgame la redundancia devolvera un true o false sirve para los condicioneles 

print(lista.index(2)) # index sirve para buscar en que casilla se encuntra el elemento marcado como parametro en este caso 2 eseta en la casilla 1 de la lista 

# valores repetidos en la lista 

print(lista.count("Luis")) # este busca el parametro asignado y devuelve en entero cuantos repetidos hay en la lista 

# como eliminar cosas en la lisata 

lista.pop() # elimina el ultimo valor de la lista cuando no tiene nada como parametro 
lista.pop(1) # parametro es el indice que deseamos eliminar 

lista.remove("Luis")# elimina un elento de la lista pero el parametro es cuando no sabemos el inidce de la lista pero sabemos que elemento se encuntra en ella 

lista.clear() # elimina todo lo de la lista 

# dar reverso ala lista 

lista.reverse() # ulitmo es primero y primero es ultimo 

# Lista[1,2,3,4,] * 2 ==> ulitplica la lista dependiendo de cuantos quereamos 

# ACOMODAR LA LISTA 

lista.sort() #acomoda la lista del menor al mayor 

lista.sort(reverse=True) # acomoda los elemntos de la lista del menor al mayor  

