print("Bienvenido a Cesar's Pizza")
print("Menu:")
print("1.- PEPPERONI")
print("2.- QUESO")
print("3.- JAMÓN")
print("4.- 4N1")
print("5.- HULA HAWAIIAN")
print("6.- ULTIMATE SUPREME")
print("7.- VEGGIE")
print("8.- 3 MEAT TREAT")
print("9.- SUPER CHEESE 4N1")
print("10.- CHICKEN BBQ") 
print("")

opcion = input("Elija su pizza. Ingrese el número de la pizza deseada: ")
cantidad = int(input("¿Cuantas pizzas desea?: "))

# Asignación de precios mejorada
if opcion == "1":
    precio = 6000
elif opcion == "2":
    precio = 7000
elif opcion == "3":
    precio = 8000
elif opcion in ["4", "5"]:
    precio = 10000
elif opcion == "6":
    precio = 11000
elif opcion in ["7", "8", "9", "10"]:
    precio = 12000

neto = precio * cantidad
iva = neto * 0.19
total = neto + iva

print(f"El neto de su pedido es {neto}")
print(f"El impuesto de su pedido es {iva}")
print(f"El total a pagar es {total}")