#determina la solucion de la siguiente exprecion logica 

a =  int(input("a -> "))
b =  int (input("b -> "))

resultado = ((3+5*8)<3) and ((-6*4)/3+(2<2))
resultado2 = (a > b)
resultado3 = resultado or resultado2 
print(f"el resultado es : {resultado3}")



