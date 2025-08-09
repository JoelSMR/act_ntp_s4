def buscar_palabras(listapalabras, letra):
    palabrasencontradas = []
    for palabra in listapalabras:
        for caracter in palabra:
            if caracter == letra:
                palabrasencontradas.append(palabra)
                break
    return palabrasencontradas

palabras = ["gato", "perro", "ratón", "pato", "caballo"]
letra = input("Ingresa la letra a buscar: ")
resultado = buscar_palabras(palabras, letra)
print("Palabras que contienen la letra '{}': {}".format(letra, resultado))