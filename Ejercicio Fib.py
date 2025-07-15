def fib(n):
    a = 0
    b = 1

    while a < n:
        print (a, end='')
        a = b
        b = a + b
        print()

    print("Fin del programa")

fib(1000)
