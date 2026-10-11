class Persona: #Creamos una clase

    def __init__(self, nombre, apellido, edad): # Se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad}")

persona1 = Persona('Lisandro', 'Alaniz', 5)
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)
print(f' El objeto1 de la clase persona es : {persona1.nombre} {persona1.apellido}, '
      f'su edad es: {persona1.edad} años')


persona2 = Persona('Gustavo', 'Alaniz', 44)
print(f' El objeto 2 de la clase persona es : {persona2.nombre} {persona2.apellido}, '
      f'su edad es: {persona2.edad} años')

persona1.nombre= 'Yamila'
persona1.apellido= 'Sabrin'
persona1.edad = 43

print(f' El objeto1 Modificado de la clase persona es : {persona1.nombre} {persona1.apellido}, '
      f'su edad es: {persona1.edad} años')

# Los atributos son: caracteríticas
# Los métodos son: el comportamiento que van a tener los objetos(acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()
