a = input("ingrese un número:")
b = input("ingrese otro número:")
a = int(a)
b = int(b)
c = a+b
print("La suma de los números ingresados es", c)
NUM = 4
type(NUM)


import random
def game():
    juego = random.choice([1,2,3,4,5,6])
    return juego
a = game()
b = game()
suma = a + b
print("el primer numero es:",a)
print("el segundo numero es:",b)
print("la suma de ambos es:",suma)
pregunta = input("Â¿desea tirar otra vez? ")
while True:
    c = game()
    d = game()
    cd = c + d
    if pregunta == "si":
        print("el primer numero es:",c)
        print("el segundo numero es:",d)
        print("la suma de ambos es:",cd)
        pregunta = input("Â¿desea tirar otra vez? ")
    elif pregunta == "no":
        print("gracias por su participaciÃ³n")
        break
    else:
        print("'si' para tirar de nuevo, 'no' para terminar el juego")
        break