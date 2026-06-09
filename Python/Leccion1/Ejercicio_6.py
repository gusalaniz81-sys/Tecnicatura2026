n_elementos = int(input("Digite la cantidad de elementos a ingresar: "))
suma_pares = 0
conteo_pares = 0
suma_impares = 0
conteo_impares = 0
for i in range(n_elementos):
    num = int(input(f"Ingrese el número {i + 1}: "))
    if num % 2 == 0:
        suma_pares += num
        conteo_pares += 1
    else:
        suma_impares += num
        conteo_impares += 1

# Calcular promedio de impares
if conteo_impares > 0:
    promedio_impares = suma_impares / conteo_impares
else:
    promedio_impares = 0

print("\nResultados:")
print("Suma de números pares:", suma_pares)
print("Cantidad de números pares:", conteo_pares)
print("Promedio de números impares:", promedio_impares)