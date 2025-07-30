# Ejercicio 5: Búsqueda de Palabras
# Implementa una función que reciba una lista de palabras y use ciclos anidados para 
# encontrar y devolver todas las palabras que contienen una letra específica ingresada por el usuario.

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