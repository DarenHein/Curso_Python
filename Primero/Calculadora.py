'''
calculadora tiene que ser funcional para ingresar ala suma resta multiplicacion y divicion debe de ser con su primera letra 

'''

op = input("Bienvenido ala calculadora de luis lee las opciones y escoje la d etu agrado \n s.Suma \n r.Resta \n m.Multiplicaion \n d.Divicion \n Digita tu opcion -> ").lower()

if op == "s" : 
    #aqui empieza lo bueno 
    print("Suma")
    num = int (input(" ingresa un numero -> "))
    num2 = int (input(" ingresa un numero -> "))
    resultado = num + num2 
    print(f"La suma de los nuemros {num} + {num2} = {resultado}")
elif op =="r" : 
        #resta 
        print("Resta")
        num = int (input(" ingresa un numero -> "))
        num2 = int (input(" ingresa un numero -> "))
        resultado = num - num2 
        print(f"La resta de los nuemros {num} - {num2} = {resultado}")
elif op =="m" :
            #multi
            print("Multiplicaion")
            num = int (input(" ingresa un numero -> "))
            num2 = int (input(" ingresa un numero -> "))
            resultado = num * num2 
            print(f"La multiplicaion de los nuemros {num} x {num2} = {resultado}")
elif op == "d" : 
       
            print("Divicion")
            num = int (input(" ingresa un numero -> "))
            num2 = int (input(" ingresa un numero -> "))
            if num2 != 0 : 
                   resultado = num / num2 
                   print(f"La Divicion de los nuemros {num} % {num2} = {resultado}")
            else : 
                    print("no se puede divir entre cero pendejo ")
            

else :
    print ("no seas pendejo ingresa un nuemro ") 