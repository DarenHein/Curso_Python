'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
'''

asignatura = ["Mate","Español","Fisica"]

cali = int(input("Cueanto sacaste en Matematicas : "))
cali2 = int(input("Cueanto sacaste en Español : "))
cali3 = int(input("Cueanto sacaste en fisica : "))

print(f"En {asignatura[0]} tiene unas nota de {cali}")
print(f"En {asignatura[1]} tiene unas nota de {cali2}")
print(f"En {asignatura[2]} tiene unas nota de {cali3}")