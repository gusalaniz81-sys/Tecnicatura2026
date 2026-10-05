# Ejercicio 8: Menú interactivo - Cajero automático
# Hacer un programa que simule un cajero automático con un saldo
# inicial de $1.000 y tendrá el siguiente menú de opciones:
#    1. Ingresar dinero en la cuenta
#    2. Retirar dinero de la cuenta
#    3. Mostrar dinero disponible
#    4. Salir

from unittest import case

saldo = 1000
while True:
    print('\t.:MENÚ:.')
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opcion = int(input("Ingrese su opcion: "))
    match opcion:
        case 1:
            monto = int(input("Ingrese el monto a depositar: "))
            saldo += monto
            print(f'Depósito realizado correctamente, Su Saldo actual es: {saldo}')
        case 2:
            retiro = int(input("Ingrese el monto a retirar: "))
            if retiro > saldo:
                print (f"Saldo insuficiente, su saldo actual es de: {saldo}")
            else:
                saldo -= retiro
                print(f'Su Saldo actual es: {saldo}')
        case 3:
            print(f'Su saldo disponible es: {saldo}')

        case 4:
            print('Salir')
            break
        case _:
            print("Opcion invalida")





