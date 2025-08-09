def registrotemperaturas():
    temperaturas = {}
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

    while True:
        print("\n1. Agregar la ciudad")
        print("2. Registrar la temperatura")
        print("3. Mostrar las estadísticas")
        print("4. Salir")
        op = input("Opción: ")

        if op == "1":
            ciudad = input("Nombre de la ciudad: ")
            if ciudad not in temperaturas:
                temperaturas[ciudad] = {}
            else:
                print("la ciudad ya existe.")
        elif op == "2":
            ciudad = input("Ciudad: ")
            if ciudad in temperaturas:
                for dia in dias:
                    temp = float(input(f"Temperatura para {dia}: "))
                    temperaturas[ciudad][dia] = temp
            else:
                print("La ciudad no existe.")
        elif op == "3":
            for ciudad, temps in temperaturas.items():
                print(f"\nCiudad: {ciudad}")
                if temps:
                    promedio = sum(temps.values()) / len(temps)
                    print(f"Promedio semanal: {promedio:.2f}")
                    print("Temperaturas por día:")
                    for dia, temp in temps.items():
                        print(f"  {dia}: {temp}")
                else:
                    print("No hay ninguna temperaturas registradas.")
        elif op == "4":
            break
