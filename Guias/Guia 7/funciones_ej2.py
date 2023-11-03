from funciones_ej1 import perteneceLetra

def borrarPosParInout(lista: list[int]):
    for num in range(0,len(lista),1):
        if num % 2 == 0:
            lista[num] = 0
            
def borrarPosParIn(lista: list[int]) -> list[int]:
    lista_final = []
    
    for num in range(0,len(lista),1):
        if num % 2 == 0:
            lista_final += [0]
        else:
            lista_final += [lista[num]]
    
    return lista_final

def sacarVocales(palabra: str) -> str:
    palabra_final = ""
    
    for num in range(0, len(palabra), 1):
        if palabra[num].lower() != "a" and palabra[num].lower() != "e" and palabra[num].lower() != "i" and palabra[num].lower() != "o" and palabra[num].lower() != "u":
            palabra_final += palabra[num]
            
    return palabra_final

def reemplazarVocales(palabra: str) -> str:
    palabra_final = ""
    
    for num in range(0, len(palabra), 1):
        if palabra[num].lower() != "a" and palabra[num].lower() != "e" and palabra[num].lower() != "i" and palabra[num].lower() != "o" and palabra[num].lower() != "u":
           palabra_final += palabra[num]
        else:
            palabra_final += "_"
            
    return palabra_final

def darVueltaPalabra(palabra: str) -> str:
    palabra_final = ""
    
    for num in range(len(palabra)-1, -1, -1):
        palabra_final += palabra[num]
    
    return palabra_final

def eliminarRepetidos(palabra: str) -> str:
    palabra_final = palabra[0]
        
    for i in range(1, len(palabra), 1):
        for j in range(0, len(palabra_final), 1):
            es_repetido = False
            
            if palabra_final[j] == palabra[i]:
                es_repetido = True
            
        if es_repetido == False:
            palabra_final += palabra[i]
        
    return palabra_final    

