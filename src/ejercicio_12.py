def palabras_unicas():
    palabras = set()
    repetidas = set()
    while True:
        palabra = input("Ingresa una palabra (o escribe 'salir' para terminar): ")
        if palabra == 'salir':
            break
        if palabra in palabras:
            repetidas.add(palabra)
        else:
            palabras.add(palabra)
    print("Cantidad de palabras únicas:", len(palabras))
    print("Palabras repetidas:", repetidas)

