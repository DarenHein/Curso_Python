# time lo vi en un video y quise ponerlo a prubea con el metodo sleep
# me recuerdan a los hilos 
import time

print("hola")
time.sleep(3) # el tiempo es en segundos no mili 
print("hola2")

# ahora vamos a ocuparlo en un for 
for i in [1,2,3,4,5,6] : 
    print(f"{i} => hola")
    time.sleep(3)

# me gusta el time en python jajajaj 
