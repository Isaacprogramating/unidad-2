# Inicialización de variables
total_bultos_livianos = 0
total_bultos_normales = 0
valor_bultos_livianos = 0
valor_bultos_normales = 0

# Solicitar al usuario la cantidad de bultos
cantidad_bultos = int(input("Ingrese la cantidad de bultos: "))

# Procesar cada bulto
for i in range(cantidad_bultos):
    while True:
        try:
            # Solicitar el peso del bulto
            peso_bulto = float(input(f"Ingrese el peso del bulto {i+1}: "))
            # Clasificar el bulto y acumular valores y contadores
            if 1 <= peso_bulto <= 5:
                total_bultos_livianos += 1
                valor_bultos_livianos += 1000
            elif 6 <= peso_bulto <= 10:
                total_bultos_normales += 1
                valor_bultos_normales += 2000
            break
        except ValueError:
            print("Por favor, ingrese un valor numérico válido para el peso del bulto.")

# Imprimir resultados
print(f"{total_bultos_livianos} bulto(s) liviano(s) ${valor_bultos_livianos}")
print(f"{total_bultos_normales} bulto(s) normal(es) ${valor_bultos_normales}")
valor_total = valor_bultos_livianos + valor_bultos_normales
print(f"Valor total a pagar: ${valor_total}")