# Ejercicio 01: Crear una función para sumar los valores recibidos de tipo
# numéricos, utilizando argumentos variables *args como parámetro de la
# función y agregar como resultado la suma de todos los valores pasados como argumentos
def sumarNum(*args):
    suma = 0
    for num in args:
        suma += num
    return suma
print(sumarNum(2,4,5,6,7,8))