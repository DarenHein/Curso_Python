# conjuntos 2 

a = set()
b = set()

a = {1,2,3,43}
b = {3,4,5,2,1,}

# se pueden igualar los conjuntos 

print( a == b) # me devolvera un booleano True False dependienddo si los conjuntos son iguales o no 

print(len(a)) # nos retorna cuantos elementos tiene el conjunto en un entero 
#---------------------------------------------------------

#union de conjuntos 

c = a | b  # esto lo que hace es que al igual que en las matematicas uno los dos conjuntos en listas solo se suman aqui es con el simbolo | el palito 
print(c)
#---------------------------------------------------------

# interseccion en conjuntos 

# solo muestra los elementos que estan en ambos conjuntos 

c = a & b # ys e pone la tecla amperson 
print(c)

#---------------------------------------------------------

#diferencia 

#los conjutos que no que se encuentran en a pero no en b 
# NOTA no es lo mismo los conjuntos que se encuentran en a pero no en b aaa los conjuntos que se encuntran en b pero no en a OJO 

c = a - b # este esta facil solo es el simbolo de menos 
c2 = b - a 
print(c) 
print(c2)

#---------------------------------------------------------

# valores simetricos 
# son valores que no comparten a y b solo imprime los que pertenecen individualmente 
c = a ^ b # pinhce simbolo culero no se como ponerlo 
print(c)

#--------------------------------------------------------

a2 = {1,2,3}
b2 = {3,4,5}
c2 = {1,2,3,4,5}

#sub conjuntos saber si un conjunto es sub conjunto de un conjunto mayor 

print(a2.issubset(c2)) # devuelve un booleano 
print(b2.issubset(c2))

# suoer conjunto 

print(c2.issuperset(a2)) # devuelve booleano 

#------------------------------------------------------

# comparten elemento en comun 

print(a2.isdisjoint(b2)) # devuve true si no comparten elemntos y false cuando comparten elementos 

# _______________________________________________________

# tambien se puede hacer inmutable un conjunto 

# para que no se puede modificar como las tuplsa 

c3 = frozenset({1,2,3})
# con el metodo frozenset el conjunto se vuvelve inmutable 

# es todo con los conjuntos 