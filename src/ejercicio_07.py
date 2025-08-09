def filtrarestudiantes(estudiantes):
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

resultado = filtrarestudiantes(estudiantes)
print("Estudiantes con promedio mayor a 8.0:", resultado)