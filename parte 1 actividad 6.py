# Ingreso de liquidación de sueldo
nom = input("Ingrese nombre empleado: ")
rut = input("Ingrese rut empleado: ")
horasTrabajadas = int(input("Ingrese las horas trabajadas: "))
valorHora = int(input("Ingrese el valor hora del empleado: "))

# Procesar la información
colacion = 5500
movilizacion = 3000
resultado = (valorHora * horasTrabajadas) + colacion + movilizacion

# Mostrar los datos de salida
print(f"-----LIQUIDACIÓN EMPLEADO----")
print(f"NOMBRE EMPLEADO: {nom}")
print(f"RUT EMPLEADO: {rut}")
print(f"MOVILIZACIÓN: {movilizacion}")
print(f"ALIMENTACIÓN: {colacion}")
print(f"PAGO A EMPLEADO: {resultado}")