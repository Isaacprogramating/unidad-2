# Solicitamos al usuario la cantidad de bultos
cantidadBultos = int(input("Ingrese la cantidad de bultos: "))

# Validamos que la cantidad de bultos sea positiva
while cantidadBultos <= 0:
    print("La cantidad de bultos debe ser mayor que cero.")
    cantidadBultos = int(input("Ingrese la cantidad de bultos: "))

# Inicializamos la variable para acumular el peso total
pesoTotal = 0

# Variable para contar los bultos ingresados
nroBulto = 1

# Ciclo while para ingresar el peso de cada bulto
while nroBulto <= cantidadBultos:
    peso = float(input(f"Ingrese el peso del bulto {nroBulto}: "))

    # Validamos que el peso sea positivo
    while peso <= 0:
        print("El peso del bulto debe ser mayor que cero.")
        peso = float(input(f"Ingrese el peso del bulto {nroBulto}: "))

    # Acumulamos el peso total
    pesoTotal += peso

    # Incrementamos el número de bulto para el próximo ciclo
    nroBulto += 1

# Mostramos el peso total de los bultos ingresados
print(f"El peso total de los {cantidadBultos} bultos es: {pesoTotal}")
