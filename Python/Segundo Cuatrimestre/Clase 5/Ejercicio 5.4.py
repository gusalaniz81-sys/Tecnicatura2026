# Ejercicio 2: Función con *args para multiplicar.
# Crear una función para multiplicar los valores recibidos
# de tipo numéricos, utilizando argumentos variables *args
# como parámetros de la función y regresar como resultado
# la multiplicación de todos los valores pasados como argumentos
def multiplicaNum(*args):
    multiplica = 1
    for num in args:
        multiplica *= num
    return multiplica
print(multiplicaNum(2,4,5))