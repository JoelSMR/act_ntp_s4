# Ejercicio 2: Sistema de Calificaciones
# Implementa una función que solicite al usuario ingresar calificaciones usando un ciclo 
# while hasta que escriba 'fin'. 
# Almacena las calificaciones en una lista y calcula el promedio, la nota más alta y más baja.


def sistema_calificaciones():
    calificaciones = []
    while True:
        entrada = input("Ingrese una calificación (o 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        try:
            calificacion = float(entrada)
            calificaciones.append(calificacion)
        except ValueError:
            print("Por favor, ingrese un número válido.")

    if calificaciones:
        promedio = sum(calificaciones) / len(calificaciones)
        nota_mas_alta = max(calificaciones)
        nota_mas_baja = min(calificaciones)

        print(f"Promedio: {promedio:.2f}")
        print(f"Nota más alta: {nota_mas_alta:.2f}")
        print(f"Nota más baja: {nota_mas_baja:.2f}")
    else:
        print("No se ingresaron calificaciones.")

sistema_calificaciones()