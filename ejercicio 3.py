def es_multiplo_de_2(parametro):
    if parametro is None:
        print("Error: El parámetro es None")
        return False
    
    if isinstance(parametro, (list, tuple, dict, set)):
        print(f"Error: El parámetro es de tipo {type(parametro).__name__}, no es un número")
        return False
    
    if isinstance(parametro, str):
        try:

            parametro = parametro.strip()
            
            if parametro == "":
                print("Error: String vacío")
                return False
            
            numero = float(parametro)
            
            if numero != int(numero):
                print("Error: El número debe ser entero para ser múltiplo de 2")
                return False
            
            numero = int(numero)
            
        except ValueError:
            print(f"Error: '{parametro}' no es un número válido")
            return False
    
    elif isinstance(parametro, (int, float)):
        if isinstance(parametro, float):
            if parametro != int(parametro):
                print("Error: El número debe ser entero para ser múltiplo de 2")
                return False
            numero = int(parametro)
        else:
            numero = parametro
    
    elif isinstance(parametro, bool):
        numero = int(parametro)
    
    else:
        print(f"Error: Tipo de dato no soportado: {type(parametro).__name__}")
        return False
    
    if numero % 2 == 0:
        print(f"✓ {numero} es múltiplo de 2")
        return True
    else:
        print(f"✗ {numero} no es múltiplo de 2")
        return False

def main():
    print(" VERIFICADOR DE MÚLTIPLOS DE 2 ")
    print("Ingresa cualquier valor para verificar si es múltiplo de 2")
    print("Escribe 'salir' para terminar\n")
    
    while True:
        entrada = input("Ingresa un valor: ")
        
        if entrada.lower() == 'salir':
            break
        
        try:
            if entrada.lower() == 'true':
                parametro = True
            elif entrada.lower() == 'false':
                parametro = False
            elif entrada.lower() == 'none':
                parametro = None
            elif entrada.startswith('[') and entrada.endswith(']'):
                parametro = eval(entrada)
            elif entrada.startswith('(') and entrada.endswith(')'):
                parametro = eval(entrada)
            elif entrada.startswith('{') and entrada.endswith('}'):
                parametro = eval(entrada)
            else:
                parametro = entrada
        except:
            parametro = entrada
        
        resultado = es_multiplo_de_2(parametro)
        print(f"Resultado: {resultado}\n")

if __name__ == "__main__":
    print("\n" + "="*50 + "\n")
    
    main()