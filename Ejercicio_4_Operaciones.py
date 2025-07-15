#Ejercicio sumar, restar, multiplicar y dividir dos numeros
#ALGORITMO
#Dos variables que guarden la información de los valores de entrada
#Una variable que guarde el resultado de la operación
#Comprobar si los valores inrtroducidos por el usuario, son numeros o no lo son (ambos deben ser numeros)
#Si son numeros, hacer la cporrespondiente operación
#Si no son numeros, mostrar un mensaje de error

import numbers

def operaciones(N1, N2):
    num1 = N1
    num2 = N2
    resultado = 0
    listaResultados = [0,0,0,0]  # [suma, resta, multiplicación, división]

    if isinstance(num1, numbers.Number) and isinstance(num2, numbers.Number):

        #Suma de dos vcalores(+
        listaResultados[0] = num1 + num2

        #Resta de dos valores(-)
        listaResultados[1] = num1 - num2

        #Multiplicación de dos valores(*)
        listaResultados[2] = num1 * num2

        #División de dos valores(/)
        listaResultados[3] = num1 / num2

        #print(listaResultados[0])
        #print(listaResultados[1])
        #print(listaResultados[2])
        #print(listaResultados[3])

        for i in range (0, len(listaResultados)):
            print("El resultado de la operación es...", listaResultados[i])
    else:
        print("ERROR")

operaciones(4, 2)