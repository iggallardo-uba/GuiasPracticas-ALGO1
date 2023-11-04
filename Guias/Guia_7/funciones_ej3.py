from math import *
from funciones_ej1 import sumaTotal

def promedio(notas: list(int)) -> int:
    return trunc(sumaTotal(notas) / len(notas))

def numerosMenoresA4(notas: list[int]) -> bool:
    for i in range(0, len(notas), 1):
        if notas[0] < 4:
            return True
    return False

def aprobado(notas: list[int]) -> int:
    if numerosMenoresA4(notas) or promedio < 4:
        return 3
    if promedio(notas) >= 4:
        if promedio(notas) >= 7:
            return 1
        return 2