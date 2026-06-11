opcion = 0
while opcion != 1:
    print('2Comprobamos que año es bisiesto')
    num = int(input('Ingrese el año: '))
    if((num % 4 ==0) and (num % 100 != 0) or num %400 ==0):
        print('El año es bisiesto')
    else:
        print('El año no es bisisesto')

    opcion = int(input('Para salir digite 1:'))
