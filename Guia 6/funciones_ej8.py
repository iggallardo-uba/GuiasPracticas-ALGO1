def p8ej1():
    x = 8
    y = 7
    x = x + y
    print("estado final: x = " + str(x) + " - y = " + str(y))

def p8ej2():
    x = 5
    y = 7
    z = x + y
    y = z * 2
    print("estado final: x = " + str(x) + " - y = " + str(y) + " - z = " + str(z))

def p8ej3():
    x = 5
    y = 7
    x = "hora"
    y = x * 2
    print("estado final: x = " + x + " - y = " + y)


def p8ej4():
    x = False
    res = not(x)
    print("estado final: x = " + str(x) + " - res = " + str(res))

def p8ej5():
    x = True
    y = False
    res = x and y
    x = res and x
    print("estado final: x = " + str(x) + " - y = " + str(y) + " - res = " + str(res))
    


