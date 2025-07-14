###1.- Realizar un programa dónde se imprima tu nombre
print("Alex")

"""Con el programa visto en la clase del viernes 11, en dónde se hacían una serie
de operaciones matemáticas, añadir lo siguiente:
 Un parámetro que sirva para identificar el operador de la función y, en
función del mismo, realizar la operación y posterior almacenamiento en la
lista.
 Añadir una nueva operación, que es el elevado (símbolo **)"""

resultados = []

def operar(a, b, operador):
    if operador == "+":
        resultado = a + b
    elif operador == "-":
        resultado = a - b
    elif operador == "*":
        resultado = a * b
    elif operador == "/":
        resultado = a / b
    elif operador == "**":
        resultado = a ** b
    else:
        print("operador no valido")
        return 
    resultados.append(resultado)
    print(f"Resultado: {resultado}")

operar(4, 8, "*")


"""3. Realizar un programa que pasándome como parámetro un número, determinar
si es múltiplo de 2 o no."""

def multiplo_dos(numero):
    if numero % 2 == 0:
        print("El número es múltiplo de 2")
    else:
        print("No es múltiplo de 2")

multiplo_dos(4)


"""4.- Realizar un programa que, pasándole como parámetro un valor, debe de realizar
las siguientes acciones:
 En caso de que el color que introduzca el usuario sea “verde” o “VERDE”,
debe de mostrarse el siguiente mensaje: “Usted puede pasar sin
problema”.
 En caso de que el color que introduzca el usuario sea “amarillo” o
“AMARILLO”, debe de mostrarse el siguiente mensaje: “Usted puede
pasar con dificultades”.
 En caso de que el color que introduzca el usuario sea “rojo” o “ROJO”,
debe de mostrarse el siguiente mensaje: “Usted no puede pasar bajo
ningún concepto”."""

def semaforo(color):
    if color.lower() == "verde":
        print("Puede pasar")
    elif color.lower() == "amarillo":
        print("Dese prisa")
    elif color.lower() == "rojo":
        print("Prohibido pasar")
    else:
        print("Color no válido")

semaforo("verde")

"""5.- Realizar un programa que cuente desde el 1 hasta el 100 (ambos incluidos) y los
imprima uno a uno."""

def cien():
    for i in range(1, 101):
        print(i)

cien()

"""6.- Realizar un programa que cuente desde el 1 hasta el 100 (ambos incluidos) e,
imprima por pantalla, sólo los números que son pares."""

def cien_pares():
    for i in range(1, 101):
        if i % 2 == 0:
            print (i)

cien_pares()

"""7.- Realizar un programa que cuente desde el 1 hasta el 100 (ambos incluidos) e,
imprima por pantalla, sólo los números que sean múltiplos de tres"""

def cien_multiplos_tres():
    for i in range(1, 101):
        if i % 3 == 0:
            print(i)

cien_multiplos_tres()

