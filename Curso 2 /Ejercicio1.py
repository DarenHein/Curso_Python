'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

'''

edad = int(input("ingresa tu edad : "))

if edad == 0 :
    print(f"no mames como vas a tener {edad}")
elif edad <= 18 and edad >= 70:
    print(f"edad adecuada{edad}")
else : 
    print(f"no cumples con los requerimientos de edad  {edad}")