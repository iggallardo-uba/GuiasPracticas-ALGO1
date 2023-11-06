path_archivos = "/home/gallardo-uba/Documents/UBA/GuiasPracticas-ALGO1/Guias/Guia_8/archivos/"

def contarLineas(nombre: str) -> int:
    archivo = open(path_archivos + nombre)
    
    return len(archivo.readlines())

def existePalabra(nombre: str, palabra: str) -> bool:
    archivo = open(path_archivos + nombre, "r")
    
    if archivo.read().count(palabra) > 0:
        return True
    
    return False

def cantidadApariciones(nombre: str, palabra: str) -> bool:
    archivo = open(path_archivos + nombre, "r")
    
    return archivo.read().count(palabra)