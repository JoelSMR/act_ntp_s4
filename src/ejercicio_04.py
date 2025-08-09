def carritocompras():
    carrito = []
    while True:
        print("\n1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar productos")
        print("4. Calcular total")
        print("5. Salir")
        op = input("Opción: ")

        if op == "1":
            nombre = input("Producto: ")
            precio = float(input("Precio: "))
            carrito.append([nombre, precio])
        elif op == "2":
            for i, prod in enumerate(carrito):
                print(f"{i+1}. {prod[0]}")
            idx = int(input("Número a eliminar: ")) - 1
            if 0 <= idx < len(carrito):
                carrito.pop(idx)
        elif op == "3":
            for prod in carrito:
                print(f"{prod[0]} - ${prod[1]:.2f}")
        elif op == "4":
            total = sum(p[1] for p in carrito)
            print(f"Total: ${total:.2f}")
        elif op == "5":
            break