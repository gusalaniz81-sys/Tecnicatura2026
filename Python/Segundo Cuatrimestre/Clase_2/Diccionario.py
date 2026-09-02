# 'Maradona': 10 Un diccionario está compuesto por dos elementos
# Una LLAVE Y UN VALOR
# dict (key, value)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'POO': 'Programación Orientada a Objetos',
    'SABD': 'Sistema de Administración de Base de Datos'
}
print(diccionario)
#Verifica la cantidad de elementos del diccionario
print(len(diccionario))

# Acceder a un diccionario con la llave(Key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificar los elementos
diccionario['IDE'] = 'Entorno de Desarrollo integral'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario:
    print(termino)

# Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys(): #Estamos usando una función
    print(termino) #Muetra solo las llaves

for valor in diccionario.values(): #Usamos una función para acceder al valor
    print(valor)

# Comprobar la existencoia de algún elementos
print('IDE' in diccionario) #Devuelve un booleano

# Agrega un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario #El diccionario se borro

#Repaso diccionario
diccionarioNuevo = {'Azul' : 'Blue', 'Rojo' : 'Red', 'Verde' : 'Green', 'Amarillo' : 'Yellow'}
print(diccionarioNuevo)
#Como eliminar
del(diccionarioNuevo['Azul'])
print(diccionarioNuevo)

#Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Lisandro' : {'Edad' : 5, 'Altura' : 1.10}, 'Bastian': [7, 1.20], 'Nicolás': [14, 1.60]}
print(diccionario2)