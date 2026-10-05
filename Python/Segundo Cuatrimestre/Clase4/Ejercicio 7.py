# Ejercicio 7: Juego de adivinar el número
# Realizar un juego para adivinar un número. Para ello se debe
# generar un número aleatorio entre 1 - 100, y luego ir pidiendo
# números indicando "es mayor" o "es menor" según sea mayor o menor
# con respecto al N. El proceso termina cuando el usuario acierta
# y allí se debe mostrar el número de intentos.
import random

num_secreto = random.randint(1,100)
intentos = 0
num = 0
while num != num_secreto:
    num = int(input("Ingrese un número: "))
    intentos += 1
    if num < num_secreto:
        print(f'El número secreto es mayor que: {num}')
    elif num > num_secreto:
        print(f'El número secreto es menor que: {num}')
    else:
        print(f'Adivinaste: el número secreto es: {num_secreto}')
        print(f'Cantidad de intentos: {intentos}')
