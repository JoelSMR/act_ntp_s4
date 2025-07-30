# Ejercicio 9: Sistema de Coordenadas
# Crea una función que simule un sistema de coordenadas. Recibe una tupla de puntos 
# (x, y) y usa ciclos para calcular la distancia total recorrida si se visitan todos los puntos en orden.

import math

def distanciatotal(puntos):
    total = 0
    for i in range(len(puntos) - 1):
        x1, y1 = puntos[i]
        x2, y2 = puntos[i + 1]
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        total += distancia
    return total

puntos = ((0, 0), (3, 4), (6, 8), (6, 2))
total = distanciatotal(puntos)
print("Distancia total recorrida:", total)