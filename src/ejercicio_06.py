import random

def puntosaleatorios():
    puntos = []
    for _ in range(10):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        puntos.append((x, y))
    return puntos

def puntosencirculo(puntos, radio=5):
    dentro = []
    for x, y in puntos:
        if (x**2 + y**2) <= radio**2:
            dentro.append((x, y))
    return dentro

# Ejemplo de uso:
puntos = puntosaleatorios()
print("Puntos generados:", puntos)
dentro = puntosencirculo(puntos)
print("Puntos dentro del círculo de radio 5:", dentro)