def sumatuplas(tupla1, tupla2):
    resultado = []
    for i in range(len(tupla1)):
        resultado.append(tupla1[i] + tupla2[i])
    return tuple(resultado)

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

suma = sumatuplas(tupla1, tupla2)
print("Suma de tuplas:", suma)