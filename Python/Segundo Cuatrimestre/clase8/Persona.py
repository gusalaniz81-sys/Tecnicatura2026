class Persona: #Esta clase hereda de la  clase Object
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self): #Override = Sobreescribir
        return f'Persona: [Nombre: {self.nombre}, Edad: {self.edad}]'

class Empleado(Persona): # Esta clase es hija de la clase persona
    def __init__(self,nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

empleado1 = Empleado('Gustavo', 44,"750000")
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)