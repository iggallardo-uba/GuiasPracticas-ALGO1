def peso_pino(altura):
    if(altura <= 3):
        return altura * 100 * 3
    else:
        return 3 * 3 * 100 + (altura - 3) * 100 * 2

def es_peso_util(peso):
    if(peso >= 400 and peso <= 1000):
        return True
    else:
        return False

def sirve_pino(altura):
    if(es_peso_util(peso_pino(altura))):
        return True
    else:
        return False
