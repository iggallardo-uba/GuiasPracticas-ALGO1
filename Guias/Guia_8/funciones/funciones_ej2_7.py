path_archivos = "/home/gallardo-uba/Documents/UBA/GuiasPracticas-ALGO1/Guias/Guia_8/archivos/"

def clonarSinComentarios(nombre: str):
    archivo = open(path_archivos + nombre, "r").readlines()
    
    lineas_escribir = []
    
    for i in range(0,len(archivo), 1):
        linea = archivo[i].lstrip()
        
        if linea[0] != "#":
            lineas_escribir.append(linea)
    
    archivo = open(path_archivos + nombre, "w")
    
    archivo.writelines(lineas_escribir)
    
    archivo.close()
    
def reverso(nombre: str):
    reverso_txt = []
    
    archivo_input = open(path_archivos + nombre, "r").readlines()
    
    archivo_output = open(path_archivos + nombre, "w")
    
    for i in range(len(archivo_input)-1, -1, -1):
        if i == len(archivo_input)-1:
            archivo_output.writelines(archivo_input[i] + "\n")
        else:
            archivo_output.writelines(archivo_input[i])
    
    archivo_output.close()

def agregarFraseFinal(nombre:str, frase:str):
    archivo = open(path_archivos + nombre, "a+")
    
    archivo.write(" " + frase)
    
    archivo.close()
        
def agregarFraseInicio(nombre:str, frase:str):
    archivo = open(path_archivos + nombre, "r")
    
    texto = archivo.read()
    
    archivo.close()
    
    archivo = open(path_archivos + nombre, "w")
    
    archivo.write(frase + " " + texto)
    
    archivo.close()
        
    