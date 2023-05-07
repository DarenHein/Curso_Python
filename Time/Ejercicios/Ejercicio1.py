#ejercicio con sentencia for 
# rappi necesita un control de vacaiones en sus empleados 
'''
son 3 claves 
clave 1 
clase 2 
clave 3 

cada clave tiene sus años de vacaciones : 

clave 1 : 
    1 año => 6 dias 
    5 años => 15 dias 
    7 años o mas => 20 dias 
clase 2 :
    1 año => 6 dias 
    5 años => 15 dias 
    7 años o mas => 20 dias 
clase 3 : 
    1 año => 6 dias 
    5 años => 15 dias 
    7 años o mas => 20 dias 

    realiza un programa que pida que clave eres y cuantos años llevas en la empresa 
'''
import time 

print(" hola solos rappi ")
nombre = input("ingresa tu nombre : ")
print("lee las opciones y escoje tu clase : ")
print("1 - clase 1 -> repartidor ")
print("2 - clase 2 -> programador ")
print("3 - clase 3 -> gerente ")
op = int(input("Digita tu opcion -> "))

if op == 1 : 
    print(f"Hola {nombre} ")
    años = int(input("ingresa la cantidad de años que llevas trabajando -> "))
    if años == 1 : 
        print(f"Hola {nombre } llevas 1 año trabajando con nostros tienes disponibles : 6 dias de vacaciones gracias ")
    elif años == 5 :
        print (f"Hola {nombre} llevas 5 años con nosotros tienes disponible : 15 dias de vacaciones gracias ")
    elif años >= 7 : 
        print(f"Hola {nombre} tienes con nostros {años} años FELICIDADES tienes -> 20 dias de vacaciones con nostros ")
    else :
        print("No vaciones dispobles por el momento gracias ")
elif op == 2 : 
    print(f"Hola {nombre}")
    años = int(input("ingresa la cantidad de años que llevas trabajando -> "))
    if años == 1 : 
        print(f"Hola {nombre } llevas 1 año trabajando con nostros tienes disponibles : 6 dias de vacaciones gracias ")
    elif años == 5 :
        print (f"Hola {nombre} llevas 5 años con nosotros tienes disponible : 15 dias de vacaciones gracias ")
    elif años >= 7 : 
        print(f"Hola {nombre} tienes con nostros {años} años FELICIDADES tienes -> 20 dias de vacaciones con nostros ")
    else :
        print("No vaciones dispobles por el momento gracias ")
elif op == 3 :
    print(f"Hola {nombre}") 
    años = int(input("ingresa la cantidad de años que llevas trabajando -> "))
    if años == 1 : 
        print(f"Hola {nombre } llevas 1 año trabajando con nostros tienes disponibles : 6 dias de vacaciones gracias ")
    elif años == 5 :
        print (f"Hola {nombre} llevas 5 años con nosotros tienes disponible : 15 dias de vacaciones gracias ")
    elif años >= 7 : 
        print(f"Hola {nombre} tienes con nostros {años} años FELICIDADES tienes -> 20 dias de vacaciones con nostros ")
    else :
        print("No vaciones dispobles por el momento gracias ")
else : 
    print("Opcion invalida digita otra vez ")

