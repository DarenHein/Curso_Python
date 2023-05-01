'''
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
'''
lista = []

op1 = int (input(" ingresa el numero :"))
op2 = int (input(" ingresa el numero :"))
op3 = int (input(" ingresa el numero :"))
op4 = int (input(" ingresa el numero :"))
op5 = int (input(" ingresa el numero :"))
op6 = int (input(" ingresa el numero :"))
op7 = int (input(" ingresa el numero :"))
op8 = int (input(" ingresa el numero :"))
op9 = int (input(" ingresa el numero :"))
op10 = int (input(" ingresa el numero :"))

lista.append(op1)
lista.append(op2)
lista.append(op3)
lista.append(op4)
lista.append(op5)
lista.append(op6)
lista.append(op7)
lista.append(op8)
lista.append(op9)
lista.append(op10)

lista.sort(reverse=True)
print(lista)