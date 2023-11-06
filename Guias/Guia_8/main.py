from funciones.funciones_ej1 import *
from funciones.funciones_ej2_7 import *
from funciones.funciones_ej19_23 import *


path_archivos = "/home/gallardo-uba/Documents/UBA/GuiasPracticas-ALGO1/Guias/Guia_8/archivos/"

salida = 1

while(salida == 1):
    print("Seleccionar el ejercicio a visualizar, para salir ingrese 0")
    
    usuario =  int(input("Num. Ejercicio: "))
    
    if(usuario == 0):
        salida = 0
    
    if(usuario == 1):
        salida_ejercicio = 1
        
        while(salida_ejercicio == 1):
            print("Los siguientes son los ejercicios del punto 2, ingrese ejercicio a ver. Para salir ingrese 0")
            print("1-contar lineas archivo \n2-existe palabra \n3-cantidad de apariciones")
            
            ejercicio = int(input("Num. Ejercicio: "))
            
            if(ejercicio == 0):
                salida_ejercicio = 0
                
            if(ejercicio == 1):
                print("el archivo de prueba es: ")
                
                archivo = open(path_archivos + "ejercicio1_1_input.txt", "r")
                print(archivo.read())
                archivo.close()
                
                print("El archivo tiene un total de " + str(contarLineas("ejercicio1_1_input.txt")) + " lineas")
                
                input("Presione enter para continuar")
                
            if(ejercicio == 2):
                print("el archivo de prueba es: ")
                
                archivo = open(path_archivos + "ejercicio1_2_input.txt", "r")
                print(archivo.read())
                archivo.close()
                
                print(existePalabra("ejercicio1_2_input.txt", input("Ingresar palabra a buscar: ")))
                
                input("Presione enter para continuar")
                             
            if(ejercicio == 3):
                print("el archivo de prueba es: ")
                
                archivo = open(path_archivos + "ejercicio1_3_input.txt", "r")
                print(archivo.read())
                archivo.close()
                
                print(cantidadApariciones("ejercicio1_3_input.txt", input("Ingresar palabra a buscar: ")))
                
                input("Presione enter para continuar")
                
    if(usuario == 2):
        salida_ejercicio = 1
        
        while(salida_ejercicio == 1):
            print("Funcion de clonar archivo de texto sin comentarios")
                
            print("el archivo de prueba es: ")
                
            archivo = open(path_archivos + "ejercicio2_1_input.txt", "r")
            print(archivo.read())
            archivo.close()
            
            clonarSinComentarios("ejercicio2_1_input.txt")
            
            print("El archivo sin comentarios y clonado es: ")
            
            archivo = open(path_archivos + "ejercicio2_1_output.txt", "r")
            print(archivo.read())
            archivo.close()
            
            input("Presione enter para salir")    
            
            salida_ejercicio = 0
         
    if(usuario == 3):
        print("Funcion de dar vuelta archivo de texto y clonarlo")
            
        print("el archivo de prueba es: ")
            
        archivo = open(path_archivos + "ejercicio3_1_input.txt", "r")
        print(archivo.read())
        archivo.close()
        
        reverso("ejercicio3_1_input.txt")
        
        print("El archivo dado vuelta y clonado es: ")
        
        archivo = open(path_archivos + "ejercicio3_1_output.txt", "r")
        print(archivo.read())
        archivo.close()
        
        input("Presione enter para salir")    
                
    if(usuario == 4):
        print("Añadir frase a final de archivo")
            
        print("el archivo de prueba es: ")
            
        archivo = open(path_archivos + "ejercicio4_1_input.txt", "r")
        print(archivo.read())
        archivo.close()
        
        agregarFraseFinal("ejercicio4_1_input.txt", "esta frase")
        
        print("El archivo con frase es: ")
        
        archivo = open(path_archivos + "ejercicio4_1_input.txt", "r")
        print(archivo.read())
        archivo.close()
        
        input("Presione enter para salir")    
        
        salida_ejercicio = 0

    if(usuario == 5):
        print("Añadir frase a final de archivo")
                
        print("el archivo de prueba es: ")
            
        archivo = open(path_archivos + "ejercicio5_1_input.txt", "r")
        print(archivo.read())
        archivo.close()
        
        agregarFraseInicio("ejercicio5_1_input.txt", "esta frase")
        
        print("El archivo con frase es: ")
        
        archivo = open(path_archivos + "ejercicio5_1_input.txt", "r")
        print(archivo.read())
        archivo.close()
        
        input("Presione enter para salir") 
        
    if(usuario == 6):
        print("Mucha paja ver como es binario") 
        
    if(usuario == 7):
        print("CSV, hay que ir por linea, despues dividir el archivo por comas y formatear cada parte y esta practicamente")
        
    if(usuario == 23):
        salida_ejercicio = 1
        
        inventario = {}
        
        while(salida_ejercicio == 1):
            print("Hay 4 opciones para el programa de inventario: ")
            print("1 - Agregar producto")
            print("2 - Actualizar stock")
            print("3 - Actualizar precio")
            print("4 - Calcular valor inventario")
            print("0 - Salir")
            print("Inventario actual: " + str(inventario.items()))
            ejercicio = int(input("Escriba su opcion: "))
            
            if(ejercicio == 0):
                salida_ejercicio = 0
                
            if(ejercicio == 1):
                agregarProducto(inventario, input("Ingrese nombre del producto: "), float(input("Ingrese precio del producto: ")), int(input("Ingrese cantidad del producto: ")))
                
            if(ejercicio == 2):
                actualizarStock(inventario, input("Ingrese nombre del producto: "), int(input("Ingrese cantidad del producto: ")))
                
            if(ejercicio == 3):
                actualizarPrecios(inventario, input("Ingrese nombre del producto: "), float(input("Ingrese precio del producto: ")))
                
            if(ejercicio == 4):
                print("El precio del inventario total es: " + str(calcularValorInventario(inventario)))
        
                input("Presione enter para seguir")
     
          