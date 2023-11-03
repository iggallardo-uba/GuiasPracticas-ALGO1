from random import *

def listaAlumnos() -> list[str]:
    termino = 0
    lista_final = []
    
    print("Puede ingresar nombres hasta poner ''listo''")
    
    while termino == 0:
        aux = input("Ingresar nombre del alumno: ")
        
        if aux != "lista":
            lista_final.append()
        else:
            termino = 1
            
def historialSube() -> list[tuple[str, int]]:
    termino = 0
    saldo = 0
    historial = []
    
    while termino == 0:
        aux = input("Opciones: C cargar credito, D descontar credito, X terminar operacion")

        if aux == "C":
            aux_saldo = input("Ingrese cantidad de saldo a cargar: ")
            saldo += aux_saldo
            historial.append(["C", aux_saldo])
            
        if aux == "D":
            aux_saldo = input("Ingrese cantidad de saldo a cargar: ")
            saldo += aux_saldo
            historial.append(["D", aux_saldo])
            
        if aux == "X":
            termino = 1
        else:
            print("Esa opcion no existe, vuelva a intentarlo")
    return historial

def eliminarNumero(lista: list[int], num: int):
    aux_lista = []
    for i in range(0, len(lista, 1)):
        if lista[i] != num:
            aux_lista.append(lista[i])
    lista = aux_lista
            

def sieteYMedio() -> list[str]:
    termino = 0
    historial = []
    valor_cartas
    cartas = [1,2,3,4,5,6,7,10,11,12]
    
    carta = choice(cartas)
    historial.append(carta)
    eliminarNumero(cartas, carta)
    
    if carta < 8:  
        valor_cartas += carta
    else:
        valor_cartas += 0.5

    print("Su primera carta es: " + carta)
    
    while termino == 0:
        eleccion = print("sus cartas son: " + historial +". Quiere sacar otra carta (escriba 1) o se planta? (escriba 2)")
        
        if eleccion == "1":
            carta = choice(cartas)
            historial.append(carta)
            eliminarNumero(cartas, carta)
            
            if carta < 8:  
                valor_cartas += carta
            else:
                valor_cartas += 0.5
            
            print("Su siguiente carta es: " + str(carta))
            
            if valor_cartas = 7.5:
                print("Usted gano")
                return historial
        
            if valor_cartas > 7.5:
                print("Usted Perdio")
                return historial
        
        elif eleccion == "2":
            print("Se termino el juego, su resumen es " + str(historial))
            return historial
        
        else:
            print("Input no valido")