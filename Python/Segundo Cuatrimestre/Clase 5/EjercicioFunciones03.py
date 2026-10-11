# Ejercicio 3: Funcion recursica
# Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el valor de 5, debe impirmir:
# 5
# 4
# 3
# 2
# 1

num = int(input("Ingrese un numero: "))

def numero_recursivo(numero):
    if numero >= 1: #Caso Base
        print(numero)
        numero_recursivo(numero - 1)
    elif numero == 0:
        return
    elif numero <= 0:
        print('Valor ingresado incorrecto...')

resultado = numero_recursivo(num)
