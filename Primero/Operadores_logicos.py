#Operadores logicos 

'''
los operadores logicos 

permiten construir operaciones logicas y devuelven un valor booleano 

son los siguientes 

And (Conjuncion ) = and 
Or (Disyuncion) = or 
Negacion = not

 **** operador and mulitplicaion logica 

true and true = true 
true and false = false 
false and true = false 
false and false = false 

*** operador or suma logica 

true or true = true 
true or false = true 
false or true = true 
false or false = false 


*** not 

not(true) = false 
not (false) = true 

priorida de operadores logicos 

1 => not
2 => and 
3 => or  


'''

#ejemplo 
num = 2 
num2 = 3 
num3 = 5 
num4 = 7 


resultado = (num == num3) and (num2 < num3) # esto mandara un booleano que es false 
print(resultado)
resultado2 = (num == num3) or (num2 < num3) # esto devolvera un valor true 
print(resultado2)
# por ultimo el not 
print(not(resultado)) # por ende devolvera un true por que negamos el false 

# la neta esta bien confuso hay que practicar mas jajajaj 