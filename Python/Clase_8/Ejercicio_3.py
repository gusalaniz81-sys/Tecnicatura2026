conteoPositivos = 0
conteoNegativos = 0
conteoNeutros = 0

for i in range(1, 11):
    num = int(input('Ingrese un numero: '))
    if num > 0:
        conteoPositivos += 1
    elif num < 0:
        conteoNegativos += 1
    else:
        conteoNeutros += 1
print('\nResultado: ')
print('Cantidad de positivos: ',conteoPositivos)
print('Cantidad de negativos: ',conteoNegativos)
print('Cantidad de neutros: ',conteoNeutros)

conteoPositivos+=1
conteoNegativos+=1