# Definimos una tupla

cocina = ("cuchara", "cuchillo", "tenedor")
print(cocina)
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])
# Mostrar de manera inversa
print(cocina[-1])


# Acceder a un rango
print(cocina[0:2])

# Ejemplo
verduras = ('papa',) # Una tupla necesita aunque sea de un elemento: la coma!
# De lo contrario solo sería un tipo str cadena

# Recorremos los elementos de una tupla
for cocinar in cocina:#Print esta usando \n para saltos de línea
    print(cocinar, end=' ') #Usamos end= para eliminar los saltos de lineas

cocinaLista = list(cocina)
cocinaLista[0] = 'plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

#del cocina #Esto es para eliminar una tupla

tupla = (4, 'Hola', 6.78, [1, 2, 3], 4, 'Hola') #Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) #Acción booleana, su respuesta es de tipo booleana
#LO que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla

#Repaso de set o conjunto
#Para definir un conjunto

conjunto2 = set()
conjunto1 = {'bye',}
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1) #Pregunta si el número 3 No está en el conjunto1

#Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) #Nos devuelve como respuesta un booleano

#Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 #La línea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 #Que elementos tienen en común
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 #Asigna el valor que está en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 #Elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2 #
print(conjunto1.issubset(conjunto3)) #Aquí preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto2.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) #Preguntamos si los elementos del conjunto1 está dentro del 3
print(conjunto3.issuperset(conjunto2)) #Si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

#Como saber si ambos conjuntos son disconexos, esto es si no comparte elementos en común
print(conjunto1.isdisjoint(conjunto2)) #No hay cosas en comun

#Convertir un conjunto totalmente en inmutable
conjunto =frozenset #Esto hace que el conjunto seatotalmente inmutable
#No se puede agregar, modificar ni eliminar elementos del conjunto