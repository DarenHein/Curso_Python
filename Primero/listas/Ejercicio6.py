'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
'''
asignatura = ["Mate","Español","Ingles"]
calificacion_minima = 6 

cali = int(input("Cuanto sacaste en Matematicas -> "))
cali2 = int(input("cuanto sacaste en Español -> "))
cali3 = int(input(f"cuanto sacaste en {asignatura[2]} -> "))

if cali >= calificacion_minima : 
    asignatura.pop(0)
elif cali2 >= calificacion_minima : 
    asignatura.pop(1)
elif cali3 >= calificacion_minima : 
    asignatura.pop(2)

# no se pudo banda aun no aprendo bucles en python pero sabia que necesitamos un bucle 