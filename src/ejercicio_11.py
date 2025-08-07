# Ejercicio 11: Crea una función que reciba dos listas y use ciclos for para convertirlas en conjuntos. Luego 
# calcula y muestra la unión, intersección, diferencia y diferencia simétrica entre ambos conjuntos.


def conjuntosbasicos(lista1, lista2):

    conjunto1 = set()
    conjunto2 = set()

    for x in lista1:
        conjunto1.add(x)

    for y in lista2:
        conjunto2.add(y)

    print("Unión:", conjunto1.union(conjunto2))

    print("Intersección:", conjunto1.intersection(conjunto2))

    print("Diferencia (conjunto1 - conjunto2):", conjunto1.difference(conjunto2))

    print("Diferencia simétrica:", conjunto1.symmetric_difference(conjunto2))


lista_a = [1, 2, 3, 4]
lista_b = [3, 4, 5,]
conjuntosbasicos(lista_a, lista_b)