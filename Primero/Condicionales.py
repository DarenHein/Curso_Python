#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

sexo = input("Indica:\n M -> mujer \n H -> hombre \n Digita tu opcion : ").lower()
nombre = input("Ingresa la primera letra de tu nombre : ")

if sexo == "m" : 
    print("eres mujer")
    print("estas en el grupo A ")
elif sexo == "h" :
    print ("eres hombre ")
    print ("estas en el grupo B ")
else : 
    print("error")
