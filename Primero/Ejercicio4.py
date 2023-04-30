# ejercicio 4 
# hacer un programa apra ingresar el radio de un circulo y se perote su area y longitud de su circunferenica 

#formulas area = pi * radio al cuadrado
# longitud = 2 * pi * radio 

pi = 3.1416 
r = float(input("ingresa el radio : "))

radio = pi * (r **2)
longitud = 2 * (pi*r)
longitud = round(longitud)# pa quitar los decimales alv 
radio = round(radio)

print(f"El radio es : {radio} \nLa longitud es : {longitud}")

