from funciones.funciones_ej1 import *


path_archivos = "/home/gallardo-uba/Documents/UBA/GuiasPracticas-ALGO1/Guias/Guia 8/archivos/"

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
                
                print("El archivo tiene un total de " + str(contarLineas("ejercicio1_1_input.txt")) + " lineas")
                
                input("Presione enter para continuar")
                
            if(ejercicio == 2):
                print("Lista a comprobar [2,8,4]")
                
                print(divideATodos([2,8,4],int(input("Ingrese numero a ver si divide: "))))
                
                input("Presione enter para continuar")   
                             
            if(ejercicio == 3):
                print("Lista a sumar [1,2,3,4,5]")
                
                print(sumaTotal([1,2,3,4,5]))
                
                input("Presione enter para continuar")

    if(usuario == 2):
        salida_ejercicio = 1
        
        while(salida_ejercicio == 1):
            print("Los siguientes son los ejercicios del punto 2, ingrese ejercicio a ver. Para salir ingrese 0")
            print("1-Cambiar numero en pos. par a 0 \n2-Borrar numero en pos. par \n3-Sacar vocales en palabra \n4-Cambiar vocales por ''_'' \n5-Dar vuelta palabra \n6-Eliominar letras repetidas")
            
            ejercicio = int(input("Num. Ejercicio: "))
            
            if(ejercicio == 0):
                salida_ejercicio = 0
                
            if(ejercicio == 1):
                ejercicio_2_1 = [0,1,2,3,4,5,6]
                
                print("lista de numeros a usar " + str(ejercicio_2_1) + " modo inout")
                print("ver codigo para ver diferencia")
                
                borrarPosParInout(ejercicio_2_1)
                
                print(ejercicio_2_1)
                
                input("Presione enter para continuar")    
            
            if(ejercicio == 2):
                ejercicio_2_2 = [0,1,2,3,4,5,6]
                
                print("lista de numeros a usar " + str(ejercicio_2_2) + " modo in")
                print("ver codigo para ver diferencia")
                
                print(borrarPosParIn(ejercicio_2_2))
                
                print("var inicio:" + str(ejercicio_2_2))
                
                input("Presione enter para continuar")        
                
            if(ejercicio == 3):
                print(sacarVocales(input("Ingresar palabra a sacar sus vocales: ")))
                
                input("Presione enter para continuar")        
                
            if(ejercicio == 4):
                print(reemplazarVocales(input("Ingresar palabra a reemplazar sus vocales: ")))
                
                input("Presione enter para continuar")      
            
            if(ejercicio == 5):
                print(darVueltaPalabra(input("Ingresar palabra a dar vuelta: ")))
                
                input("Presione enter para continuar")    
            
            if(ejercicio == 6):
                print(eliminarRepetidos(input("Ingresar palabra a borrar letras repetidas: ")))
                
                input("Presione enter para continuar")        
                
    if(usuario == 3):
        salida_ejercicio = 1
        
        while(salida_ejercicio == 1):
            print("Los siguientes son los ejercicios del punto 3, ingrese ejercicio a ver. Para salir ingrese 0")
            print("1-alguno es 0 \n2-ambos son 0 \n3-es nombre largo \n4-es_bisiesto")
            
            
            input("Presione enter para continuar")
                
    if(usuario == 4):
        salida_ejercicio = 1
        
        while(salida_ejercicio == 1):
            print("Los siguientes son los ejercicios del punto 3, ingrese ejercicio a ver. Para salir ingrese 0")
            print("1-peso pino \n2-es peso util pino 0 \n3-sirve el pino")
            
            ejercicio = int(input("Num. Ejercicio: "))
            
            if(ejercicio == 0):
                salida_ejercicio = 0
                
            if(ejercicio == 1):
                
            
                input("Presione enter para continuar")

    if(usuario == 5):
        salida_ejercicio = 1
        
        while(salida_ejercicio == 1):
            print("Los siguientes son los ejercicios del punto 3, ingrese ejercicio a ver. Para salir ingrese 0")
            print("1-devolver el doble si es par\n2-si es impar, devolver el siguiente numero \n3-devolver el triple si es multiplo de 9 y el doble si es multiplo de 3 \n4-lindo nombre\n5-El rango\n6-Vacaciones o chamba")
            
            ejercicio = int(input("Num. Ejercicio: "))
            
            if(ejercicio == 0):
                salida_ejercicio = 0
                
            if(ejercicio == 1):
                
                input("Presione enter para continuar")