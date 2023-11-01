import time

def p6ej1():
    numero = 1

    while(numero < 11):
        print(numero)
        numero += 1

def p6ej2():
    numero = 10

    while(numero < 41):
        print(numero)
        numero += 2

def p6ej3():
    numero = 1
    while(numero < 11):
        numero += 1
        print("eco")

def p6ej4(numero):
    while(numero >= 1):
        print(numero)
        numero -= 1
        time.sleep(1)

    print("Despegue")

def p6ej5(partida, llegada):
    while(partida > llegada):
        partida -= 1
        print("Viajó un año al pasado, estamos en el año: " + str(partida))
        time.sleep(2)

def p6ej6(partida):
    print("pendiente por paja")


