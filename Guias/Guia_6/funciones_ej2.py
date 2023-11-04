from math import sqrt, ceil

def imprimir_saludo(nombre):
    print("Hola %s" % nombre)
    
def raiz_cuadrada_de(numero):
    print(round(sqrt(numero),4))
    
def fahrenheit_a_celsius(temp_far):
    print(round(((temp_far-32)*(5/9)), 4))
    
def imprimir_dos_veces(estribillo):
    print(estribillo * 2)
    
def es_multiplo_de(numero, multiplo):
    if(multiplo%numero==0):
        return True
    else:
        return False
    
def es_par(numero):
    if(es_multiplo_de(2, numero) == True):
        return True
    else:
        return False
    
def cantidad_de_pizzas(comensales, min_porciones):
    cant_pizzas = str(ceil((comensales*min_porciones)/8))
    print("Se necesitan un total de " + cant_pizzas +  " Pizzas")