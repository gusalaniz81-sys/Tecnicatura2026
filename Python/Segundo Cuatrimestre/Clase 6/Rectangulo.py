"""
Creamos una clase llamada rectángulo, debe tener 2 atributos: altura y base
el nombre del método será calcular area utilizando la formula:
area = base * altura. Pero la base y la altura deben ser ingresada por el usuario
y los objetos deben ser tres.
"""
class Rectangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
    def calcular_area (self):
        return self.base * self.altura

altura = int(input('Ingrese la altura: '))
base = int(input('Ingrese la base: '))
resultado = Rectangulo(altura, base)

print(f'El área del rectángulo es: {resultado.calcular_area()}')

altura2 = int(input('Ingrese la altura2: '))
base2 = int(input('Ingrese la base2: '))
resultado2 = Rectangulo(altura2, base2)
print(f'El area del rectangulo es: {resultado2.calcular_area()}')

altura3 = int(input('Ingrese la altura3: '))
base3 = int(input('Ingrese la base3: '))
resultado3 = Rectangulo(altura3, base3)
print(f'El area del rectangulo es: {resultado3.calcular_area()}')