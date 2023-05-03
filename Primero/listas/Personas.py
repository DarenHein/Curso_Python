# voy a trtara de hacer una lista de personas 

lista_Persona = ["luis" , 30 ,1.65 , 83.5 , "Masculino "]
persona2 = []

print("Hola bienvenido a mi programa de practica de listas lee las opciones y elije la de tu agrado : ")
print (" 1 - Buscar por nombre ")
print (" 2 - Eliminar una persona ")
print (" 3 - Agregar una persona ")
print (" 4 - Imprimir datos de la persona ")
op = int (input("Digita tu opcion : "))

if op == 1 : 
    nombre =  input ("ingresa el nombre de la persona que deseas buscar ")
    if nombre == lista_Persona[0] : 
        print(f"La persona se encunetra en nuestra base de datos {lista_Persona[0]}")
    else :
        print("Lo lamento la persona no se encuentra en nuestros registros desea agregarla : ")
        op2 = int(input("1 - si \n2 - no \n Digita tu opcion :  "))
        if op2 == 1 :
            nombre2 = input("ingresa el nombre de la persona a agregar : ")
            persona2.append(nombre2)
            print = (f"la persona a si agregada con exito ! ")
        else : 
            print("adios")
elif op == 2 : 
    print(f"Eliminar persona \n la persona registara en este momento es : ")
    print(f"Nombre : {lista_Persona[0]}")
    print(f"edad : {lista_Persona[1]}")
    print(f"altura : {lista_Persona[2]}")
    print(f"peso : {lista_Persona[3]}")
    print(f"sexo : {lista_Persona[4]}")
    op3 = int (input(f"Deseas eliminarla ? \n 1 si \n 2 no \n Digita tu opcion : "))
    if op3 == 1 : 
        lista_Persona.clear()
        print("La persona a sido eliminada con exito adios ")
    else : 
        print("adios")
elif  op ==3 : 
    print("Agregar persona : ")
    nombre = input("ingresa el nombre de la persona : ")
    edad = int(input("ingresa la edad de la persona : "))
    altura =  input("ingresa la altura de la persona : ")
    sexo = input("Ingresa el sexo de la persona : ")
    persona2.append(nombre)
    persona2.append(edad)
    persona2.append(altura)
    persona2.append(sexo)
    print(f"la persona registrada cumple con los siguientes atributos {persona2}")
    print("adios")
    # aqui poner di deseamos modificar algun parametro en el futuro
elif op == 4 : 
    print("hola")
    # aqui mostrar los datos de las persons que se vallan registrando pero necesitamos buclas para que vallan guardando en memoria 
    print(f"La persona registrada es la siguiente : {lista_Persona}")
    print("por el momento solo contamos con esa persona en un futuro deseamos poder agregar mas memoria jejej gracias por ocupar nuestro programa :) ")
else : 
    print("opcion invalida ")









