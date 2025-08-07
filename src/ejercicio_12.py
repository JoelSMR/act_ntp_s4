# Ejercicio 12: Implementa una función que solicite al usuario ingresar palabras usando un ciclo while hasta 
# que escriba 'salir'. Almacena las palabras en un conjunto y muestra cuántas palabras únicas se 
# ingresaron y cuáles se repitieron.


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

