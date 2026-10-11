# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celsius
# a fahrenheit y viseversa
# Investigar las fórmulas
grados = float(input("Ingrese la temperatura en grados Celsius: "))
def convertidorCelsius (celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit
resultado = convertidorCelsius(grados)
print(f'{grados} grados Celsius equivalen a {resultado} grados Fahrenheit')

gradosFahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
def convertidorFahrenheit (fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
resultado2 = convertidorFahrenheit(gradosFahrenheit)
print(f'{gradosFahrenheit} grados Fahrenheit equivalen a {resultado2} grados Celsius')