nota = float(input('Ingrese la nota del 1 al 10: '))
if nota == 9 or nota == 10:
    print('La calificación es A')
elif 8 <= nota < 9:
    print('La calificacion es B')
elif 7 <= nota < 8:
    print('La calificacion es C')
elif 6 <= nota < 7:
    print('La calificacion es D')
elif 0 < nota < 6:
    print('La calificacion es F')
else:
    print('La nota ingresada es incorrecta')





