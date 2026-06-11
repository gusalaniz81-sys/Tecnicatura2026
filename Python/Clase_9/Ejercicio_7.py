i = 1
suma = 0
while i <= 5:
    print(f'\nSalario del empleado: {i}')
    horas = float(input('Ingrese las horas trabajadas: '))
    tarifa = float(input('Ingrese la tarifa por hora: '))

    salario = horas * tarifa

    print(f"El salario es: ${salario}")

    suma = suma + salario

    i = i + 1
print(f"\nLa suma de todos los salarios es: ${suma}")