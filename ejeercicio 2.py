def calcular(num1, num2, operador):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        return num1 / num2 if num2 != 0 else None
    elif operador == '**':
        return num1 ** num2
    else:
        return None

resultados = []
operadores = ['+', '-', '*', '/', '**']

print("Calculadora - Operadores disponibles:", ', '.join(operadores))

while True:
    entrada = input("Operación (ej: 5 + 3) o 'salir': ").strip()
    
    if entrada.lower() == 'salir':
        break
    
    operador = None
    partes = []
    
    if '**' in entrada:
        partes = entrada.split('**')
        operador = '**'
    elif '+' in entrada:
        partes = entrada.split('+')
        operador = '+'
    elif '-' in entrada:
        partes = entrada.split('-')
        operador = '-'
    elif '*' in entrada:
        partes = entrada.split('*')
        operador = '*'
    elif '/' in entrada:
        partes = entrada.split('/')
        operador = '/'
    
    if not operador or len(partes) != 2:
        print("Formato inválido")
        continue
    
    try:
        num1, num2 = float(partes[0]), float(partes[1])
        resultado = calcular(num1, num2, operador)
        
        if resultado is None:
            print("Error en la operación")
        else:
            operacion = f"{num1} {operador} {num2} = {resultado}"
            resultados.append({'operacion': operacion, 'operador': operador})
            print(f"Resultado: {operacion}")
            
    except ValueError:
        print("Error: números inválidos")

if resultados:
    print(f"\nResumen ({len(resultados)} operaciones):")
    for i, item in enumerate(resultados, 1):
        print(f"{i}. {item['operacion']}")
else:
    print("No se realizaron operaciones")