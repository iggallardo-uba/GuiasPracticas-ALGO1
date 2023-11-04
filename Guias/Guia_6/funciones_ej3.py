def alguno_es_0(num1, num2):
    if(num1 == 0 or num2 == 0):
        return True
    else:
        return False
    
def ambos_son_0(num1, num2):
    if(num1 == 0 and num2 == 0):
        return True
    else:
        return False
    
def es_nombre_largo(nombre):
    if(len(nombre) >= 3 and len(nombre) <= 8):
        return True
    else:
        return False

def es_bisiesto(anio):
    if(anio % 4 == 0 and anio % 100 != 0):
        return True
    else:
        return False