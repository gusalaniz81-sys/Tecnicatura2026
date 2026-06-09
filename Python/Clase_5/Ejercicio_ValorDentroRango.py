valor = int(input("Ingrese un numero: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = valor >= valorMinimo and valor <= valorMaximo
if dentroRango:
    print(f'El valor {valor} está dentro del rango')
else:
    print(f'El valor {valor} No está dentro del rango')
