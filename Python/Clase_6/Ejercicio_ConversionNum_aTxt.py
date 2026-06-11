num = int(input("Ingrese un numero en el rango del 1 al 3: "))
numTexto = ''
if num ==1:
    numTexto = 'Numero uno'
elif num == 2:
    numTexto = 'Numero dos'
elif num == 3:
    numTexto = 'Numero tres'
else:
    numTexto = 'Has ingresado un número fuera del rango'
print(f'El número ingresado es : {num} - {numTexto}')
