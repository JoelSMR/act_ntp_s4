# Ejercicio 3: Combinación de Listas
# Crea una función que reciba dos listas de igual tamaño y use un ciclo for para combinarlas 
# elemento por elemento en una nueva lista. Ejemplo: [1,2,3] + ['a','b','c'] = [1,'a',2,'b',3,'c'].

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