
import numbers

def fib(numero):
    #Precondición: El valor de valor de entrada debe de ser un numéro entero

    #Definición de las variables a emplear
    a = 0
    b = 1

    #Se comprueba que el valor de entrada es un número entero
    #si el valor no es un número, entonces se le dice al usuario que el valor es incorrecto.
    #en caso de que no, pues se ejecuta el algoritmo.
    if isinstance(numero, numbers.Number):
        print("es un número")

        while a < numero:
                print(a, end='')
                a = b
                b = a + b
                
                #Valores de salida
                print()
                    
        print("fin del programa")

    else:
        print("no es número")
        print("el programa ha finalizado por que no se ha introducido un valor válido")


fib(4536)
