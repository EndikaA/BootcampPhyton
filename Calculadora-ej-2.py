
while True:
    print("\n--- CALCULADORA ---")
    
    # Pedir números
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    op = input("Operación (+, -, *, /, **): ")
    
    # Hacer la operación
    if op == "+":
        resultado = a + b
    elif op == "-":
        resultado = a - b
    elif op == "*":
        resultado = a * b
    elif op == "/":
        resultado = a / b
    elif op == "**":
        resultado = a ** b
    else:
        print("Operación no válida")
        continue
    
    # Mostrar resultado
    print("Resultado:", resultado)
    

