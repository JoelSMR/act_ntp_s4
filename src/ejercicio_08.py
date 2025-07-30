# Ejercicio 8: Secuencia de Fibonacci
# Implementa una función que cree una tupla con los primeros 20 números de la secuencia de Fibonacci. Usa 
# un ciclo while para generar la secuencia y luego un ciclo for para mostrar solo los números impares.

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