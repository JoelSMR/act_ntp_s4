def agendatelefonica():
    agenda = {}
    while True:
        print("\n1. Agregar un contacto")
        print("2. Buscar un contacto")
        print("3. Mostrar todos los contactos")
        print("4. Eliminar un contacto")
        print("5. Salir")
        op = input("Opción: ")

        if op == "1":
            nombre = input("Nombre: ")
            tel = input("Teléfono: ")
            agenda[nombre] = tel
        elif op == "2":
            nombre = input("Nombre a buscar: ")
            if nombre in agenda:
                print(f"{nombre}: {agenda[nombre]}")
            else:
                print("No encontrado.")
        elif op == "3":
            for nombre, tel in agenda.items():
                print(f"{nombre}: {tel}")
        elif op == "4":
            nombre = input("Nombre a eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
            else:
                print("No encontrado.")
        elif op == "5":
            break
