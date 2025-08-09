
def combinarlistas(lista1, lista2):
    nuevalista = []
    for i in range(len(lista1)):
        nuevalista.append(lista1[i])
        nuevalista.append(lista2[i])
    return nuevalista

# Ejemplo de uso:
listaa = [1, 2, 3]
listab = ['a', 'b', 'c']
resultado = combinarlistas(listaa, listab)
print(resultado) 