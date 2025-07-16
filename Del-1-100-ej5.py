import numbers
# precondicion: el valor de entrada debe ser un número entero
def sumar (numero):
    a = 1
    
    if isinstance(numero, numbers.Number):
        while a < numero:
            print(a, end= "\n")
            a += 1
        print("fin del programa <3")
    else:
        print("El valor de entrada debe ser un número entero")

sumar(101)  # Llamada a la función con el número 101 para que permita sumar hasta 100
            