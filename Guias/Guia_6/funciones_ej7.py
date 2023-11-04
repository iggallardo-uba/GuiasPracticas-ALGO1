import time

def p7ej1():
    for num in range(1,11,1):
        print(num)

def p7ej2():
    for num in range(10,41,2):
        print(num)

def p7ej3():
    for num in range(1,11,1):
        print("eco")

def p7ej4(numero):
    for num in range(numero,1,-1):
        print(num)
        time.sleep(1)
    print("Despegue")


def p7ej5(partida, llegada):
    for num in range(partida-1,llegada+1,-1):
        print("Viajó un año al pasado, estamos en el año: " + str(num))
        time.sleep(2)

def p7ej6(partida):    
    print("pendiente por paja")
