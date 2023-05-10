'''
calculadora que sume reste multiplique potencie y resto 
con menu de opciones y solo dos valores 

'''

while True : 
    print("Calculadora lee las opciones y escoje la que necesitas ")
    print("1 -> suma ")
    print("2 -> resta")
    print("3 -> multiplicaion ")
    print("4 -> divicion")
    print("5 -> potenciacion ")
    print("6 -> resto ")
    op = int(input("Digita tu opcion : "))
    if op == 1 : 
        num = int (input("ingresa un numero : "))
        num2 = int(input("ingresa otro numero : "))
        num += num2
        print(f"el resultado de la suma es {num}")
    elif op == 2 :
        num = int (input("ingresa un numero : "))
        num2 = int(input("ingresa otro numero : "))
        num -= num2
        print(f"el resultado de la resta es {num}") 
    elif op == 3 : 
        num = int (input("ingresa un numero : "))
        num2 = int(input("ingresa otro numero : "))
        num *= num2
        print(f"el resultado de la multiplicaion es {num}") 
    elif op == 4 : 
        num = int (input("ingresa un numero : "))
        num2 = int(input("ingresa otro numero : "))
        if num2 == 0 : 
            print(" no se puede dividir entre cero pendejo ")
        else : 
            num /= num2 
            print(f"el resultado de la dicivion es {num}") 
    elif op == 5 : 
        num = int (input("ingresa un numero : "))
        num2 = int(input("ingresa otro numero : "))
        num **= num2
        print(f"el resultado de la potencia es {num}")
    elif op == 6 : 
        num = int (input("ingresa un numero : "))
        num2 = int(input("ingresa otro numero : "))
        num %= num2
        print(f"el resultado de la resto es {num}")
else : 
    print(f"numero no valido")
print("")

