def gestioncalificaciones():
    estudiantes = {}
    while True:
        print("\n1. Agregar un estudiante")
        print("2. Agregar una calificación")
        print("3. Calcular el promedio")
        print("4. Mostrar todos los estudiantes")
        print("5. Salir")
        op = input("Opción: ")

        if op == "1":
            nombre = input("Nombre del estudiante: ")
            if nombre not in estudiantes:
                estudiantes[nombre] = []
            else:
                print("Ya existe ese estudiante.")
        elif op == "2":
            nombre = input("Nombre del estudiante: ")
            if nombre in estudiantes:
                cal = float(input("Calificación: "))
                estudiantes[nombre].append(cal)
            else:
                print("No existe ese estudiante.")
        elif op == "3":
            nombre = input("Nombre del estudiante: ")
            if nombre in estudiantes and estudiantes[nombre]:
                promedio = sum(estudiantes[nombre]) / len(estudiantes[nombre])
                print(f"Promedio de {nombre}: {promedio:.2f}")
            else:
                print("No hay calificaciones para ese estudiante.")
        elif op == "4":
            for nombre, cals in estudiantes.items():
                print(f"{nombre}: {cals}")
        elif op == "5":
            break
