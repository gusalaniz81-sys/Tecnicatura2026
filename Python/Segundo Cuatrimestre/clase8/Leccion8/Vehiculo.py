"""
Definir una clase padre llamada vehículo y dos clases llamadas
Auto y Bicicleta, las cuales heredan de la clase padre Vehiculo.
LA clase padre debe tener los siguientes atributos y métodos:

Vehículo (clase padre)
-Atributos(color, ruedas)
-Métodos(__init__(color, rueda) y __str__()

Auto(clase hija de vehúlo)
-Atributos (velocidad (km/hr))
_Método(__init__(color, rueda, velocidad) y __str__))

Bicicleta(clase hija de vehículo)
_Atributos(tipo(urbana/montaña/etc.)
-Método (__init__(color, ruedas, tipo) y __str__()

Crear un objeto de cada clase
"""
class Vehiculo:
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def ruedas(self):
        return self._ruedas

    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas

    def __str__(self):
        return f'color: {self._color}, ruedas: {self._ruedas}'

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self._velocidad = velocidad
    def __str__(self):
        return f'Vehiculo: [Color: {self._color}, Ruedas: {self._ruedas}, Velocidad: {self._velocidad}]'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo
    def __str__(self):
        return super().__str__() + f' tipo: {self._tipo}'


vehiculo1 = Vehiculo('Azul', 4)
print(vehiculo1)

vehiculo2 = Auto('Verde', 4, 100)
print(vehiculo2)

vehiculo3 = Bicicleta('Vermelho', 2, 'montania')
print(vehiculo3)