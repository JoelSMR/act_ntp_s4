def contarduplicados(lista):
    numerosunicos = set()
    for num in lista:
        numerosunicos.add(num)
    duplicados = len(lista) - len(numerosunicos)
    print("Números originales:", len(lista))
    print("Números únicos:", len(numerosunicos))
    print("Cantidad de duplicados:", duplicados)
