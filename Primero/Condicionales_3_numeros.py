#realizar un programa que lea 3 numreos y diga caul es el mayor de los 3 

a  = int (input("digita un numero : "))
b  = int (input("digtia el segundo numero : "))
c  = int (input ("digita el ultimo numero : "))

if a>b and a>c : 
    print (f"el nuermo mayor es el {a}")
elif b>a and b>c : 
    print (f"el numero mayor es {b}")
elif c>b and c>a : 
    print(f"el numero mayor ess {c}")
else : 
    print("los 3 numero son iguales")