# Ejercicio 5: Factorial de un número positivo
# Hacer un programa para calcular el factorial de un número postivo

factorial = 1
numero = int(input('Ingrese un número: '))
if numero > 0:
    for i in range(1, numero + 1):
        factorial = factorial * i
    print(f'La factorial es: {factorial}')
else:
    print('El numero es negativo')

