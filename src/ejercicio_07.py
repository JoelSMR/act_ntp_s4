# Ejercicio 7: Filtrado de Estudiantes
# Desarrolla una función que reciba una tupla de estudiantes (nombre, edad, promedio) y use un ciclo 
# for para encontrar y devolver una nueva tupla solo con los estudiantes que tienen promedio mayor a 8.0.

def filtrar_estudiantes(estudiantes):
    estudiantesfiltrados = []
    for estudiante in estudiantes:
        nombre, edad, promedio = estudiante
        if promedio > 8.0:
            estudiantesfiltrados.append(estudiante)
    return tuple(estudiantesfiltrados)

# Ejemplo de uso:
estudiantes = (
    ("Ana", 20, 9.1),
    ("Luis", 22, 7.5),
    ("Sofía", 19, 8.5),
    ("Carlos", 21, 7.9)
)

resultado = filtrar_estudiantes(estudiantes)
print("Estudiantes con promedio mayor a 8.0:", resultado)