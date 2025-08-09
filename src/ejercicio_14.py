def sistemavotacion():
    votos = set()
    while True:
        voto = input("Vota por un candidato (o escribe 'fin' para terminar): ")
        if voto.lower() == "fin":
            break
        votos.add(voto)
    print("Candidatos que recibieron votos:")
    for candidato in votos:
        print(candidato)