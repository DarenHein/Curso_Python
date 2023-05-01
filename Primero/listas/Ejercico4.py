
'''
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
'''

loteria = []

op = int(input("ingresa el nuemro de la loteria : "))
op2 = int (input("ingresa el segundo numero de la loteria  : "))

loteria.append(op)
loteria.append(op2)
loteria.sort()
print(loteria)
