#Ejercicio sumar, restar, multiplicar y dividir dos numeros

#ALGORITMO
#Dos variables que guarden la informacion  de los valores de entrada.
#comprobar si los valores introducidos por los usuarios son numeros o no
    #SI son numeros, hacer la correspondiente operacion
    #Si no, escribir "parametros de entrada no validos"


import numbers

def operaciones(variable1, variable2):
    num1 = variable1
    num2 = variable2
    resultado = 0
    listaResultados = [0,0,0,0]

    if isinstance(num1, numbers.Number) and isinstance(num2, numbers.Number):
        print("")

        #suma de valores
        listaResultados[0] = num1 + num2

        #resta de dps valores
        listaResultados[1] = num1 - num2

        #multiplicacion de dos valores
        listaResultados[2] = num1 * num2

        #division de dos valores
        listaResultados[3] = num1 / num2

        for i in range (0, len(listaResultados)):
            print("El resultado de la operacion es...")
            print(listaResultados[i])

    else:
        print("ERROR")

operaciones(4,2)