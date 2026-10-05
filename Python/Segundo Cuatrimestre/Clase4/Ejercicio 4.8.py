# Ejercicio 3: Insertar elementos y ordenarlos
# Pedir números y meterlos en una lista, cuando el usuario
# Introduzca un número 0, nuestro programa dejaría de insertar.
# Por último, mostrar los números ordenados de menor a mayor

lista = []
salir = False
while not salir:
    numero = int(input('Ingrese un numero: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort() # La lista queda ordenada con esta función
print(f'\nLista ordenada: \n{lista}')