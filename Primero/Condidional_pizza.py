'''
Ejercicio 10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
'''

print("Bienvvenidoas ala pizeria Napoli \n lee nuestro menu y escoje tu tipo de pizza")
print ("1 Vegetariana")
print ("2 No vegetariana ")
op = int (input("digita tu opcion : "))
if op == 1 : 
    print("Menu pizza vegetariana")
    print("Contamos con los siguientes ingredientes solo puedes escojer unon : \n 1 pimiento \n 2 tofu ")
    op2 = int(input("Digita tu opcion : "))
    if op2 == 1 : 
        print("Gracias por tu compra la pizza lleva los siguientes ingredientes \n 1 -> pimiento \n 2 -> mozzarella \n 3 -> Tomate  ")
    elif op2 == 2 : 
        print("Gracias por tu compra la pizza lleva los siguientes ingredientes \n 1 -> Tofu \n 2 -> mozzarella \n 3 -> Tomate  ")
    else : 
        print ("opcion equivocada ")
elif op == 2 :
    print ("Menu pizza no Vegetariana")
    print("Contamos con los siguientes ingredientes solo puedes escojer unon : \n 1 peperoni \n 2 jamon \n 3 salmon  ")
    op2 = int (input("Digita tu opcion : "))
    if op2 == 1 : 
        print("Gracias por tu compra la pizza lleva los siguientes ingredientes \n 1 -> peperoni \n 2 -> mozzarella \n 3 -> Tomate  ")
    elif op2 == 2 :
        print("Gracias por tu compra la pizza lleva los siguientes ingredientes \n 1 -> jamon \n 2 -> mozzarella \n 3 -> Tomate  ")
    elif op2 == 3 : 
        print("Gracias por tu compra la pizza lleva los siguientes ingredientes \n 1 -> salmon \n 2 -> mozzarella \n 3 -> Tomate  ")
    else : 
        print("opcion incorrecta gracias")

else :
    print (" error ")