'''
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

'''
dic = {"nombre":"" ,"edad":"","direccion":"","telefono":""}
nom = input("ingresa tu nombre -> ")
dic ["nombre"] = nom
ed = int(input("ingresa tu edad -> "))
dic["edad"] = ed
addres = input("ingresa tu direccion -> ")
dic["direccion"] = addres
cel = input("ingresa tu numeto de cel. -> ")
dic["telefono"] = cel
print(f"nombre -> {dic['nombre']}")
print(f"edad -> {dic['edad']}")
print(f"Direccion -> {dic['direccion']}")
print(f"Tel. -> {dic['telefono']}")
