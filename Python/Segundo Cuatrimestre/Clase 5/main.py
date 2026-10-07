# Desempaquetar una lista o lits Unpacking
from Tools.demo.beer import bottle


def show(nombre, apellido):
    print(nombre+' '+apellido)
persona = ["Lisandro", "Alaniz"]
show(persona[0], persona[1]) #Pasamos uno por uno los datos de la lista a la función
show(*persona)# Esto es lo mismo que lo anterior pero le pasamos TODO JUNTO
persona2 =("Bastian",'Alaniz') # Desempaquetamos a travez de una tupla
show(*persona2)
persona3 = {"nombre":"Bastian", "apellido":"Alaniiz"}
show(**persona3)

numbers = [1, 2, 3, 4, 5, 6] #Aún con la lista vacia se ejecuta el ELSE
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la única manera que no se ejecute el ELSE
else:
    print('Esto se terminó')

### List comprehension, lista de comprensión
names = ['Lisandro', 'Basti', 'Nico', 'Lucila']
along = [p for p in names if p[0] == 'L']
print(along)

bottleC =[{'name':'Quilmes', 'country': 'Arg'},
          {'name':'Corona', 'country': 'Mx'},
          {'name':'Setlla Artois','country':'Belgium'}]
Arg = [p for p in bottleC if p['country'] == 'Arg']
print(Arg)
print(bottleC)

### Paso de argumentos (funciones)
def mi_func(nombre, apellido):
    print('Saludos a todos')
    print(f'Nombre:{nombre}, Apellido:{apellido}')
mi_func("Lisandro", "Alaniz")
mi_func("Basti", "Alaniz")

### La palabra return en funciones
## Creamos una función para sumar
def sumar(a, b):
    return a + b
resultado = sumar(78, 22)
print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(24, 26)}')

def sumar2(a = 0, b = 0): # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f'El resultado de la suma es: {resultado}')
print(f'Resultado de la suma es: {sumar2(24, 26)}')

## Argumento, variables en funcion
def listaNombres(*nombres):
    for nombre in nombres:
        print(nombre)
listaNombres("Lisandro", "Bastian","Nico", 'Lucila')
listaNombres("Agustín", "Ivan", 'Nicol')

###
def listarTerminos(**terminos): #Lo más utilizados **kwargs para recibir los argumentos
    for llave, valor in terminos.items(): #kwargs significa: key word arguments
        print(f'{llave}: {valor}')

listarTerminos() # NO recibe nada, nada se va a mostrar
listarTerminos(IDE='Integrad Develoment Enviroment', PK='Primary Key' )
listarTerminos(Nombre= 'Leonel Messi')
