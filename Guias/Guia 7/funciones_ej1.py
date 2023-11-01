def perteneceNum(lista: list[int], numero: int) -> bool:
    for i in lista:
        if i == numero:
            return True
    return False

def divideATodos(lista: list[int], numero: int) -> bool:
    for i in lista:
        if i % numero != 0:
            return False
    return True

def sumaTotal(lista: list[int]) -> int:
    num = 0
    
    for i in lista:
        num += i
    return num

#def ordenados

def mayor7letras(palabra: str) -> bool:
    if len(palabra) > 7:
        return True
    return False

def palindromo(palabra: str) -> bool:
    for num in range(0,len(palabra)/2,1):
        if palabra[0+num] != palabra[len(palabra)-num]:
            return False
    return True

def contrasenia(contra: str) -> str:
    if len(contra) < 5:
        return "ROJA"
    if len(contra) < 8:
        return "AMARILLA"
    
    aux = False
    
    for letra in contra:
        if letra.isupper():
            aux = True
    
    if aux == False:
        return "AMARILLA"
    
    aux = False
    
    for letra in contra:
        if letra.islower():
            aux = True
    
    if aux == False:
        return "AMARILLA"
    
    aux = False
    
    for letra in contra:
        if letra.isdigit():
            aux = True
    
    if aux == False:
        return "AMARILLA"
    
    return "VERDE"
            
def movimientosBancarios(movimientos: list[tuple[str, int]]) -> int:
    saldo = 0
    
    for movimiento in movimientos:
        if movimiento[0] == "I":
            saldo += movimiento[1]
        else:
            saldo -= movimiento[1]
    return saldo
    