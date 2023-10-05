from funciones_ej1 import *
from funciones_ej2 import *
from funciones_ej3 import *

salida = 1

while(salida == 1):
    print("Seleccionar el ejercicio a visualizar, para salir ingrese 0")
    
    usuario =  int(input("Num. Ejercicio: "))
    
    if(usuario == 0):
        salida = 0
    
    if(usuario == 1):
        print("Los siguientes son los ejercicios del punto 1")

        imprimir_hola_mundo()

        imprimir_un_verso()

        raizDe2()

        factoria_de_dos()

        perimetro()

    if(usuario == 2):
        salida_ejercicio = 1
        
        while(salida_ejercicio == 1):
            print("Los siguientes son los ejercicios del punto 2, ingrese ejercicio a ver. Para salir ingrese 0")
            print("1-imprimir saludo \n2-raiz cuadrada de \n3-Fahrenheit a celsius \n4-Imprimir dos veces estribillo \n5-Es multiplo de \n6-Es par \n7-Cantidad de Pizzas")
            
            ejercicio = int(input("Num. Ejercicio: "))
            
            if(ejercicio == 0):
                salida_ejercicio = 0
                
            if(ejercicio == 1):
                imprimir_saludo(input("Ingrese nombre a saludar: "))
                
                input("Presione enter para continuar")
            
            if(ejercicio == 2):
                raiz_cuadrada_de(int(input("Ingrese numero a realizar raiz cuadrada: ")))
                
                input("Presione enter para continuar")
                
            if(ejercicio == 3):
                fahrenheit_a_celsius(int(input("Ingrese temp. Farhenheit para convertir: ")))
                
                input("Presione enter para continuar")
                
            if(ejercicio == 4):
                estribillo = "Dale a tu cuerpo alegría, Macarena \nQue tu cuerpo es pa' darle alegría y cosa buena \nDale a tu cuerpo alegría, Macarena \nEh, Macarena (¡ay!)\n"
                imprimir_dos_veces(estribillo)
                
                input("Presione enter para continuar")
            
            if(ejercicio == 5):
                multiplo = es_multiplo_de(int(input("Numero a chequear su multiplo: ")), int(input("Su multiplo a chequear: ")))
                
                if(multiplo == True):
                    print("El numero es multiplo")
                else:
                    print("el numero no es multiplo")
                    
                input("Presione enter para continuar")
            
            if(ejercicio == 6):
                par = es_par(int(input("Ingrese numero a ver si es par: ")))
                
                if(par == True):
                    print("El numero es par")
                else:
                    print("el numero no es par")
                    
                input("Presione enter para continuar")
                
            if(ejercicio == 7):
                cantidad_de_pizzas(int(input("Ingrese cantidad de personas: ")), int(input("Ingrese la cantidad de porciones por persona: ")))
                    
                input("Presione enter para continuar")
                
    if(usuario == 3):
        salida_ejercicio = 1
        
        while(salida_ejercicio == 1):
            print("Los siguientes son los ejercicios del punto 3, ingrese ejercicio a ver. Para salir ingrese 0")
            print("1-alguno es 0 \n2-ambos son 0 \n3-es nombre largo \n4-es_bisiesto")
            
            ejercicio = int(input("Num. Ejercicio: "))
            
            if(ejercicio == 0):
                salida_ejercicio = 0
                
            if(ejercicio == 1):
                algun0 = alguno_es_0(int(input("Ingrese el primer numero: ")), int(input("Ingrese el segundo: ")))
                
                if(algun0 == True):
                    print("Uno de los numeros fue 0")
                else:
                    print("Los dos numeros no son 0")
                    
                input("Presione enter para continuar")
                
            if(ejercicio == 2):
                algun0 = ambos_son_0(int(input("Ingrese el primer numero: ")), int(input("Ingrese el segundo: ")))
                
                if(algun0 == True):
                    print("Ambos numeros son 0")
                else:
                    print("Alguno de los numeros no es 0")
                    
                input("Presione enter para continuar")
            
            if(ejercicio == 3):
                nomlargo = es_nombre_largo(input("Ingrese su nombre: "))
                
                if(nomlargo == True):
                    print("Es un nombre largo")
                else:
                    print("Es un nombre raro")
                    
                input("Presione enter para continuar")
                
            if(ejercicio == 4):
                bis = es_bisiesto(int(input("Ingrese el año: ")))
                
                if(bis == True):
                    print("Es un año bisiesto")
                else:
                    print("No es un año bisiesto")
                    
                input("Presione enter para continuar")
                
    if(usuario == 4):
        salida_ejercicio = 1
        
        while(salida_ejercicio == 1):
            print("Los siguientes son los ejercicios del punto 3, ingrese ejercicio a ver. Para salir ingrese 0")
            print("1-alguno es 0 \n2-ambos son 0 \n3-es nombre largo \n4-es_bisiesto")
            
            ejercicio = int(input("Num. Ejercicio: "))
            
            if(ejercicio == 0):
                salida_ejercicio = 0
                
            if(ejercicio == 1):
                algun0 = alguno_es_0(int(input("Ingrese el primer numero: ")), int(input("Ingrese el segundo: ")))
                
                if(algun0 == True):
                    print("Uno de los numeros fue 0")
                else:
                    print("Los dos numeros no son 0")
                    
                input("Presione enter para continuar")
            
            if(ejercicio == 2):
                algun0 = alguno_es_0(int(input("Ingrese el primer numero: ")), int(input("Ingrese el segundo: ")))
                
                if(algun0 == True):
                    print("Uno de los numeros fue 0")
                else:
                    print("Los dos numeros no son 0")
                    
                input("Presione enter para continuar")
                
            if(ejercicio == 3):
                algun0 = alguno_es_0(int(input("Ingrese el primer numero: ")), int(input("Ingrese el segundo: ")))
                
                if(algun0 == True):
                    print("Uno de los numeros fue 0")
                else:
                    print("Los dos numeros no son 0")
                    
                input("Presione enter para continuar")
                
    if(usuario == 5):
        salida_ejercicio = 1
        
        while(salida_ejercicio == 1):
            print("Los siguientes son los ejercicios del punto 3, ingrese ejercicio a ver. Para salir ingrese 0")
            print("1-alguno es 0 \n2-ambos son 0 \n3-es nombre largo \n4-es_bisiesto")
            
            ejercicio = int(input("Num. Ejercicio: "))
            
            if(ejercicio == 0):
                salida_ejercicio = 0
                
            if(ejercicio == 1):
                algun0 = alguno_es_0(int(input("Ingrese el primer numero: ")), int(input("Ingrese el segundo: ")))
                
                if(algun0 == True):
                    print("Uno de los numeros fue 0")
                else:
                    print("Los dos numeros no son 0")
                    
                input("Presione enter para continuar")  
                
                
                
                