def semaforo(color):

    color = color.lower()
    
    if color == "verde":
        print("Usted puede pasar sin problema")
    elif color == "amarillo":
        print("Usted puede pasar con dificultades")
    elif color == "rojo":
        print("Usted no puede pasar bajo ningún concepto")
    else:
        print("Color no válido. Use: verde, amarillo o rojo")

while True:
    entrada = input("Ingrese el color del semáforo (o 'salir'): ").strip()
    
    if entrada.lower() == 'salir':
        break
    
    semaforo(entrada)