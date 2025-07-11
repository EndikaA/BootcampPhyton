#Ejercicio sumar, restar, multiplicar y dividir dos números.

#ALGORITMO
#Dos variables que que guarden la información de los valores de entrada.
#Una variable que guarden el resultado de la operacion
#Comprobar si los valores introducidos por el usuario, son números o no son (ambos)
    #Si son numeros, hacer la correspondiente operación.
    #Si no, escribir "parametros de entrada no válidos"



import numbers

def operaciones(N1, N2):
    num1 = N1
    num2 = N2
    resultado = 0
    listaResultados = [0,0,0,0]

    if isinstance(num1, numbers.Number) and isinstance(num2, numbers.Number):
        
        #Suma de dos valores (+)
        listaResultados[0]= num1 + num2
        
        #Resta de dos valores (-)
        listaResultados[1] = num1 - num2

        #Multiplicación de dos valores (*)
        listaResultados[2] = num1 * num2

        #División de dos valores (/)
        listaResultados[3] = num1 / num2

        for i in range (0, len(listaResultados)):
            print("El resultado de la operación es..")
            print(listaResultados[i])

    else:
        print("ERROR")

operaciones(4,2)