def operacionesconjuntos():
    pares = set()
    multiplosde3 = set()

    for i in range(2, 21):
        if i % 2 == 0:
            pares.add(i)

    for i in range(3, 31):
        if i % 3 == 0:
            multiplosde3.add(i)

    print("Conjunto de los pares:", pares)
    print("Conjunto de los múltiplos de 3:", multiplosde3)
    print("Unión:", pares | multiplosde3)
    print("Intersección:", pares & multiplosde3)
    print("Diferencia entre (pares - múltiplos de 3):", pares - multiplosde3)
    print("Diferencia entre (múltiplos de 3 - pares):", multiplosde3 - pares)
    print("Diferencia simétrica:", pares ^ multiplosde3)
