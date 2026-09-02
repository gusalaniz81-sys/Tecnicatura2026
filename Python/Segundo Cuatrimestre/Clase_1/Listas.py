# Listas = Gustavo, Lisandro, Yamila, Bastian
# Colecciones en Python

#Las listas es lo que se conoce en otros Lenguajes como Arreglos o Vectores

nombres = ['Lisandro', 'Yamila', 'Bastian', 'Nicolás']
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[-1])
print(nombres[0:2]) # Solo muestra el índice 0, 1 pero no el indice 2
print(nombres[:3]) # Indices a mostrar 0, 1, 2
#Desde el índice indicado hasta el final
print(nombres[1: ])
# Modificamos un valor
nombres[3] = 'Iván'
nombres[0] = 'Lichi'
print(nombres)
#Iterar lista
for nombre in nombres: # Nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')
# Preguntamos cuantos elementos tienen la lista
print(len(nombres)) # Le psamos como parámetro la lista

# Agregar un elemento
nombres.append('Nicolas')
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)

# Insertar un elementos en un indice específico
nombres.insert(1, 'Yamila')
print(nombres)
nombres.insert(3, 'Gustavo')
print(nombres)

# Eliminar un elemento
nombres.remove('Yamila')
print(nombres)

#Eliminar el último elemento de la lista
nombres.pop()
print(nombres)

# Eliminar un indice específico
del nombres[1]
print(nombres)

#Eliminar, borar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
#del nombres
print(nombres)

# Concatenar listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2 #Concatenamos
print(lista3)

lista3.extend([7, 8, 9, 1]) #Función para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) #Función para ubicar en que índice está el valor ingresado
# print(lista3.index(0)) esto daría un error por no ser el elementos parte de la lista

#Como sabemos cuantos valores están repetidos en una lista
print(lista3.count(1)) #Cuenta cuantos valores iguales hay dentro de la lista

#Para poner al revez la lista
lista3.reverse()
print(lista3)

#Para que una lista se multiplique repitiendo sus elementos
lista3 =lista3 * 2
print(lista3)

#Métodos de ordenamiento
lista3.sort() # ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True) #Ordena descendentemente
print(lista3)

