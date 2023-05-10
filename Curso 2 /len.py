'''
la funcion len tiene la funcion de retornar el numero de caracteres que lo componen 


importante : tambien cuenta los espacios asi que teemos que restarlos por eso en la liena linea 9 tiene un - 1
por q restamos el espacio  

'''
cadena = "hola mundo"
conta = len(cadena) - 1
print(f" la palabra {cadena} contiene {conta} caracteres " )

'''
ejemplo 2 

ingrese una palabra por teclado y diga los caracteres de esta 

'''

palabra = input("ingresa una palabra y ve de cuantos caracteres esta compuesta : ")
contador = len(palabra)
print(f"la palabra contiene : {contador} -> caracteres")