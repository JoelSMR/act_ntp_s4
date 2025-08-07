# Ejercicio 13: Desarrolla una función que genere dos conjuntos: uno con números pares del 2 al 20 
# y otro con múltiplos de 3 del 3 al 30.Usa ciclos for para crear 
# los conjuntos y muestra todas las operaciones entre ellos.

def operaciones_conjuntos():
    pares = set()
    multiplos3 = set()

    for i in range(2, 21):
        if i % 2 == 0:
            pares.add(i)

    for i in range(3, 31):
        if i % 3 == 0:
            multiplos3.add(i)

    print("Conjunto de los pares:", pares)
    print("Conjunto de los múltiplos de 3:", multiplos3)
    print("Unión:", pares | multiplos3)
    print("Intersección:", pares & multiplos3)
    print("Diferencia entre (pares - múltiplos de 3):", pares - multiplos3)
    print("Diferencia entre (múltiplos de 3 - pares):", multiplos3 - pares)
    print("Diferencia simétrica:", pares ^ multiplos3)
