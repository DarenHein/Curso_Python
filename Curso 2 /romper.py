'''
continue y break

es como el break de java en switch sirve para terminar el programa tambien puedo hacer casos con esto 

'''
import time 
print("")
while True : 

    print(" lee las opciones y escoje la de tu agrado : ")
    print("1 . op ")
    print("2 . op  ")
    print("3 . op ")

    op = int(input("digita tu opcion : "))
    if op == 1 : 
        print("hola")
    elif op ==2 : 
        print("adios")
    elif op ==3 :
        print("hola")
    else : 
        print("opcion invalida")

    print("Deseas salir del programa ")
    print(" 1 si")
    print(" 2 no ")
    op2 = int(input("Digita tu opcion : "))
    if op2 == 1 : 
        break
    else :
        print("")
    