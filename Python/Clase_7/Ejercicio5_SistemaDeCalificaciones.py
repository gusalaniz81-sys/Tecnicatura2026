calificacion = float(input('Ingrese un valor del 0 al 10: '))
if (9 <= calificacion <= 10):
    print(f'La calificacion es A')
elif (8< calificacion < 9):
    print(f'La calificacion es B')
elif (7< calificacion < 8):
    print(f'La calificacion es c')
elif (6< calificacion < 7):
    print(f'La calificacion es D')
elif (6 > calificacion > 0):
    print(f'La calificacion es F')
else:
    print('El Valor ingresado es incorrecto')