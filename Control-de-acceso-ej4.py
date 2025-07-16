#Control de acceso basado en el color
# El usuario introduce un color y el programa le indica si puede pasar o no
while True:
    print("\n --- CONTROL DE ACCESO ---")

    #Pedir color
    a = input("Introduce el color: ")
    
    if isinstance(a, str):
        # Comprobar el color
        # Convertir a minúsculas para evitar problemas de mayúsculas/minúsculas 
        if a.lower() == "rojo":
            print("Usted no puede pasar bajo ningún concepto")
        elif a.lower() == "verde":
            print("Usted puede pasar sin problema")
        elif a.lower() == "amarillo":
            print("Usted puede pasar, con dificultades")
        else:
            print("Color no reconocido")
