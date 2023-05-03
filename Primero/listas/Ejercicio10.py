#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

print("para poder pagar los inpustos necesitamos saber tu edad y cuanto gans al mes ")
edad = int (input(" Ingresa tu edad : "))
ingresos = int(input(" ingresa tu ingreso mensual : ")) 

if edad >= 18 and ingresos >= 1000 : 
    print("erer candidato a pagar inpuestos ")
else:
    print("no pagas perro felicidades ") 
    