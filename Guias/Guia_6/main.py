from funciones_ej1 import *
from funciones_ej2 import *
from funciones_ej3 import *
from funciones_ej4 import *
from funciones_ej5 import *
from funciones_ej6 import *
from funciones_ej7 import *
from funciones_ej8 import *

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
            print("1-peso pino \n2-es peso util pino 0 \n3-sirve el pino")
            
            ejercicio = int(input("Num. Ejercicio: "))
            
            if(ejercicio == 0):
                salida_ejercicio = 0
                
            if(ejercicio == 1):
                print("La altura del pino es " + str(peso_pino(int(input("Ingrese la altura del pino: ")))))
            
                input("Presione enter para continuar")

            if(ejercicio == 2):
                if(es_peso_util(int(input("Ingrese el peso del pino: ")))):
                    print("El pino es bueno para la fabrica")
                else:
                    print("el pino no sirve para la fabrica")
                    
                input("Presione enter para continuar")
                
            if(ejercicio == 3):
                if(sirve_pino(int(input("Ingrese la altura del pino: ")))):
                    print("El pino sirve para la fabrica")
                else:
                    print("El pino no sirve para la fabrica")
                    
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
                print("El numero final es: " + str(devolver_el_doble_si_es_par(int(input("Ingrese numero a chequear: ")))))
                input("Presione enter para continuar")

            if(ejercicio == 2):
                print("El numero final es: " + str(devolver_valor_si_es_par_si_no_el_que_sigue(int(input("Ingrese numero a chequear: ")))))
                input("Presione enter para continuar")

            if(ejercicio == 3):
                print("El numero final es: " + str(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(int(input("Ingrese numero a chequear: ")))))
                input("Presione enter para continuar")

            if(ejercicio == 4):
                lindo_nombre(input("Ingrese nombre a chequear: "))
                input("Presione enter para continuar")

            if(ejercicio == 5):
                elRango(int(input("Ingrese numero a chequear: ")))
                input("Presione enter para continuar")

            if(ejercicio == 6):
                vacaciones(int(input("Ingrese edad de la persona: ")), input("Ingrese sexo de la persona(F o M): "))
                input("Presione enter para continuar")

    if(usuario == 6):
        salida_ejercicio = 1
        
        while(salida_ejercicio == 1):
            print("Los siguientes son los ejercicios del punto 6, ingrese ejercicio a ver. Para salir ingrese 0")
            print("1-numeros del 1 al 10 \n2-numeros pares del 10 al 40 \n3-eco 10 veces \n4-cuenta regresiva\n5-Viaje en el tiempo\n6-Viaje en el tiempo hasta Aristoteles")
            
            ejercicio = int(input("Num. Ejercicio: "))
            
            if(ejercicio == 0):
                salida_ejercicio = 0

            if(ejercicio == 1):
                print("El output de la funcion es: ")
                p6ej1()
                input("Presione enter para continuar")

            if(ejercicio == 2):
                print("El output de la funcion es: ")
                p6ej2()
                input("Presione enter para continuar")

            if(ejercicio == 3):
                print("El output de la funcion es: ")
                p6ej3()
                input("Presione enter para continuar")
            
            if(ejercicio == 4):
                p6ej4(int(input("Ingrese inicio de la cuenta regresiva: ")))
                input("Presione enter para continuar")

            if(ejercicio == 5):
                p6ej5(int(input("Ingrese año de partida: ")), int(input("Ingrese año de llegada: ")))
                input("Presione enter para continuar")

            if(ejercicio == 6):
                p6ej6(int(input("Ingrese año de partida: ")))
                input("Presione enter para continuar")

    if(usuario == 7):
        salida_ejercicio = 1
        
        while(salida_ejercicio == 1):
            print("Los siguientes son los ejercicios del punto 7, ingrese ejercicio a ver. Para salir ingrese 0")
            print("1-numeros del 1 al 10 \n2-numeros pares del 10 al 40 \n3-eco 10 veces \n4-cuenta regresiva\n5-Viaje en el tiempo\n6-Viaje en el tiempo hasta Aristoteles")
            
            ejercicio = int(input("Num. Ejercicio: "))
            
            if(ejercicio == 0):
                salida_ejercicio = 0

            if(ejercicio == 1):
                print("El output de la funcion es: ")
                p7ej1()
                input("Presione enter para continuar")

            if(ejercicio == 2):
                print("El output de la funcion es: ")
                p7ej2()
                input("Presione enter para continuar")

            if(ejercicio == 3):
                print("El output de la funcion es: ")
                p7ej3()
                input("Presione enter para continuar")
            
            if(ejercicio == 4):
                p7ej4(int(input("Ingrese inicio de la cuenta regresiva: ")))
                input("Presione enter para continuar")

            if(ejercicio == 5):
                p7ej5(int(input("Ingrese año de partida: ")), int(input("Ingrese año de llegada: ")))
                input("Presione enter para continuar")

            if(ejercicio == 6):
                p7ej6(int(input("Ingrese año de partida: ")))
                input("Presione enter para continuar")

    if(usuario == 8):
        salida_ejercicio = 1
        
        while(salida_ejercicio == 1):
            print("Los siguientes son los ejercicios del punto 8, ingrese ejercicio a ver. Para salir ingrese 0")
            print("1 \n2 \n3 \n4 \n5")
            
            ejercicio = int(input("Num. Ejercicio: "))
            
            if(ejercicio == 0):
                salida_ejercicio = 0
            
            if(ejercicio == 1):
                print("Este es la ejecucion del codigo: ")
                p8ej1()
                input("Presione enter para continuar")

            if(ejercicio == 2):
                print("Este es la ejecucion del codigo: ")
                p8ej2()
                input("Presione enter para continuar")

            if(ejercicio == 3):
                print("Este es la ejecucion del codigo: ")
                p8ej3()
                input("Presione enter para continuar")

            if(ejercicio == 4):
                print("Este es la ejecucion del codigo: ")
                p8ej4()
                input("Presione enter para continuar")

            if(ejercicio == 5):
                print("Este es la ejecucion del codigo: ")
                p8ej5()
                input("Presione enter para continuar")

    if(usuario == 9):
        salida_ejercicio = 1
        
        while(salida_ejercicio == 1):
            print("Los siguientes son los ejercicios del punto 9, ingrese ejercicio a ver. Para salir ingrese 0")
            print("1-alguno es 0 \n2-ambos son 0 \n3-es nombre largo \n4-es_bisiesto")
            
            ejercicio = int(input("Num. Ejercicio: "))
            
            if(ejercicio == 0):
                salida_ejercicio = 0      
                
                