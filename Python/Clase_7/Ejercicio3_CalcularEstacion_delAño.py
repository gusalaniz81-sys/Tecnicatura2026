mes = None
while mes == None:
    mesAño = int(input("Ingrese un mes de año (1/12) o (0) salir: "))
    if mesAño == 0:
        mes = 1
        break
    if (1 <= mesAño <= 3):
        print(f'verano 21/12 al 12/03')
    elif (4 <= mesAño <= 6):
        print(f'Otoño 21/03 al 12/06')
    elif (7 <= mesAño <= 9):
        print(f'Invierno 21/06 al 12/09')
    elif (10<= mesAño <= 12):
        print(f'Primavera 21/09 al 12/12')
    else:
        print('Número invalido, ingresar del 1 al 12')
