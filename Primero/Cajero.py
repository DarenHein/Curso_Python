'''
Crear un cajero automatico con menu 
que el menu tenga lo siguiente 
1 sacar dinero 
2 ingresar dinero 
3 chehcar saldo 
5 salir 

'''

saldo = 1000
op = int (input("Cajero \n lee las opciones y escoje la de agrado : \n 1 -> ingresar dinero \n 2 -> retirar dinero \n 3 -> consultar saldo \n 4 salir alv  "))

if op == 1 : 
    print ("Deposito de dinero ")
    op2 = int (input("Cuento dinero desea ingresar -> "))
    resultado = saldo + op2 
    print (f" el saldo depositado es de {op2} \n saldo total actualmente -> {resultado}")
elif op == 2 : 
    print ("Retiro de dinero ")
    op2 = int(input("ingresa la cantidad que desea sacar -> "))
    resultado = saldo - op2
    print (f"Saldo retirado {op2} saldo total : {resultado}")
elif op == 3 : 
    print("consulta de saldo ")
    print (f"saldo actual {saldo}")
elif op == 4 : 
    print ("adios")
else : 
    print ("valor incalivo")