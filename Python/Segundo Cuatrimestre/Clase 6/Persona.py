class Persona: #Creamos una clase

    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): # Se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni #Este atributo está encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self): #self es igual a this de java
        print(f"La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad},"
                  f" la direccion es: {self.args}, los datos importantes son {self.kwargs}")

#Self solo se encuentra dentro de los métodos

persona1 = Persona('Lisandro', 'Alaniz', 58871169, 5)
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)
print(f' El objeto 1 de la clase persona es : {persona1.nombre} {persona1.apellido}, '
      f'su edad es: {persona1.edad} años')


persona2 = Persona('Gustavo', 'Alaniz', 44001087, 44)
print(f' El objeto 2 de la clase persona es : {persona2.nombre} {persona2.apellido}, '
      f'su edad es: {persona2.edad} años')

#Así modificamos los attributos de un objeto
persona1.nombre= 'Yamila'
persona1.apellido= 'Sabrin'
persona1.edad = 43
print(f' El objeto 1 Modificado de la clase persona es : {persona1.nombre} {persona1.apellido}, '
      f'su edad es: {persona1.edad} años')

# Los atributos son: caracteríticas
# Los métodos son: el comportamiento que van a tener los objetos(acciones)
persona1.mostrar_detalle() #De ésta manera llamamos al método def mostrar_detalle
persona2.mostrar_detalle() # LA referencia en este caso se pasa de forma automática

Persona.mostrar_detalle(persona1) #Debemos pasarle una referencia para el self # o dará error

persona3 = Persona('Agustin', 'Alaniz', 33445566, 26,'Telefono', '33445566', 'calle Mburucuya', 1252,
                   'Manzana', 22, 'casa', 20, Altura=1.74, Peso=82, CFavorito='RAcingClub', Auto='SinAunto', Modelo='n/n')
persona3.mostrar_detalle()
#print(persona3._dni) #Esto no se debe utilizar (está encapsulado) esto dice que lo desconocemos Python.
#persona3.__nombre # Está totalmente encapsulado