# las tuplas igual que las listas son conjunto de elemntos estas se diferencian de las lisats por que son inmodificables NO SE PUEDEN MODIFICAR 

# sintaxis : 
# tupla = (1,2,3,4,"hola",(hola,3),True) 
# las tuplas van entre parentesis y como las listas pueden almacenar cualquier tipo de adtos String boooleano y entero 

'''
las tuplas no se pueden agregar elemntos ni borrar elementos como en las lisats osea
no se puede ocupar append ni pop 

'''

tupla = (1,2,3,4,5,6) #tupla de enteros 
print(tupla[0]) #asi como en las listas se puede mandar a llamr al valor en especifo de la tupla 
print (4 in tupla) # buscar un valor ¿ el 4 esta en tupla ?
print (tupla.index(1)) # nos retorna el indice donde se encuntra lo que pusimo en el parametro 
print(tupla.count(2)) # retorna cuantos repetidos hay en la tupla 
print (len(tupla)) # nos indica cuantos elementos hay en la tupla 

lista = list(tupla)# de tupla a lista 

# de lista a tupla 
tupla = tuple(lista) 