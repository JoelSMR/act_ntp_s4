def fibonacci20():
    fib = []
    a, b = 0, 1
    while len(fib) < 20:
        fib.append(a)
        a, b = b, a + b
    return tuple(fib)

secuencia = fibonacci20()
print("Secuencia de Fibonacci:", secuencia)

print("Números impares en la secuencia:")
for num in secuencia:
    if num % 2 != 0:
        print(num)