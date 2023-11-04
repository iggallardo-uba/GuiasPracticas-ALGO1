from funciones_ej2 import es_par, es_multiplo_de

def devolver_el_doble_si_es_par(numero):
    if(es_par(numero)):
        return numero * 2
    else:
        return numero

def devolver_valor_si_es_par_si_no_el_que_sigue(numero):
    if(es_par(numero)):
        return numero
    else:
        return numero + 1

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero):
    if(es_multiplo_de(9, numero)):
        return numero * 3
    elif(es_multiplo_de(3,numero)):
        return numero * 2
    else:
        return numero
    
def lindo_nombre(nombre):
    if(len(nombre) >= 5):
        print("Tu nombre tiene muchas letras")
    else:
        print("Tu nombre tiene menos de 5 caracteres")

def elRango(numero):
    if(numero < 5):
        print("Menor a 5")
    elif(numero >= 10 and numero <= 20):
        print("Entre 10 y 20")
    elif(numero > 20):
        print("Mayor a 20")
    else:
        print("Otro")

def vacaciones(edad, sexo):
    if(sexo == "M"):
        if(edad < 18 or edad >= 65):
            print("Andá de vacaciones")
        else:
            print("Te toca chambear")
    else:
        if(edad < 18 or edad >= 60):
            print("Andá de vacaciones")
        else:
            print("Te toca chambear")
