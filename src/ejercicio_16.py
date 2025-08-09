def frecuenciapalabras(frase):
    frase = frase.lower()
    palabras = frase.split()
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    ordenadas = sorted(conteo.items(), key=lambda x: x[1], reverse=True)
    for palabra, frequencia in ordenadas:
        print(f"{palabra}: {frequencia}")
