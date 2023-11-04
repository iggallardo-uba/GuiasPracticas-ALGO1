def perteneceNum(lista: list[int], numero: int) -> bool:
    for i in lista:
        if i == numero:
            return True
    return False

def perteneceLetra(palabra: str, letra: str) -> bool:
    for i in palabra:
        if i == letra:
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

def mayor7letras(lista: list[str]) -> bool:
    for palabra in lista:
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

def masDe3Vocales(palabra: str) -> bool:
    bool_a = False
    bool_e = False
    bool_i = False
    bool_o = False
    bool_u = False
    
    cant_vocales = 0
    
    for letra in palabra:
        if letra.lower() == "a" and bool_a == False:
            bool_a = True
            cant_vocales += 1    
            
        if letra.lower() == "e" and bool_e == False:
            bool_e = True
            cant_vocales += 1    
            
        if letra.lower() == "a" and bool_i == False:
            bool_i = True
            cant_vocales += 1    
            
        if letra.lower() == "a" and bool_o == False:
            bool_o = True
            cant_vocales += 1    
            
        if letra.lower() == "a" and bool_u == False:
            bool_u = True
            cant_vocales += 1   
            
        if cant_vocales >= 3:
            return True 
    
    return False
    