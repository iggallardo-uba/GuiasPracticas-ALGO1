from ...Guia_7.funciones_ej1 import perteneceLetra

path_archivos = "/home/gallardo-uba/Documents/UBA/GuiasPracticas-ALGO1/Guias/Guia 8/archivos/"

def contarLineas(nombre: str) -> int:
    archivo = open(path_archivos + nombre)
    
    return len(archivo.readlines())