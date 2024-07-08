print("Ingrese los siguientes datos para realizar su compra")
nombre = input("Nombre: ")
telefono = input("Teléfono: ")
print("Ingrese producto y cantidad")
producto = input("Nombre del producto: ")
cantidad = input("Cantidad: ")
print("¿Está seguro que desea pagar? ('s' o 'n'): ")
opcion = input()

if opcion.lower() == "s":
    if not nombre or not telefono or not producto or not cantidad:
        print("\nFaltan datos por ingresar. Toda la información es obligatoria. Por favor chequee la información ingresada.")
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {telefono}")
        print(f"Producto: {producto}")
        print(f"Cantidad: {cantidad}")
        print("\nVuelva a comenzar")
    else:
        print("\nLa compra se ha realizado con éxito. Muchas gracias por su compra.\n")
else:
    print("\nLa compra no se ha realizado. No se ha realizado ningún cobro.\n")