#Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste exactamente sí (en minúsculas y con tilde)

op = int (input (" desea regresar el programa \n 1 si \n 2 no "))

while op != 2 : 
    op = int (input (" desea regresar el programa \n 1 si \n 2 no "))

print("adios")