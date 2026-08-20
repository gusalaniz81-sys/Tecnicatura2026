# Listas = Gustavo, Lisandro, Yamila, Bastian
nombres = ['Lisandro', 'Yamila', 'Bastian', 'Nicolás']
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[-1])
print(nombres[0:2]) # Solo muestra el índice 0, 1 pero no el indice 2
print(nombres[:3]) # Indicews a mostrar 0, 1, 2
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
del nombres
print(nombres)