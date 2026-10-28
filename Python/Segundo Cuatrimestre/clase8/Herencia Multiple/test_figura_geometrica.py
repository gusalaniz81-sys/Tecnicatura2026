from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creacion de objeto Clase Cuadrado'.center(50,'_'))
cuadrado1 = Cuadrado(8, 'azul')
cuadrado1.alto = -10
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f'Calculo del área del cuadrado: {cuadrado1.calcular_area()}')

#MRO = Method Resolution Orden
print(Cuadrado.mro())

print(cuadrado1)
print('Creacion de objeto Clase Cuadrado'.center(50,'_'))
rectangulo1 = Rectangulo(3, 9,'verde')
rectangulo1.ancho = 15
print(F'Calculo del area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)