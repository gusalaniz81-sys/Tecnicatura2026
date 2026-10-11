
def factorial(numero):
    if numero == 1: #Caso Base
        return 1
    else:
        return numero * factorial(numero - 1)
numeroFactorial = int(input("Ingrese un numero para calcular el factorial: "))
resultado = factorial(numeroFactorial)
print(f'El factorial del número {numeroFactorial} es: {resultado}')