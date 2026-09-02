# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8) #Definimos la tupla
#Crear una lista que solo incluya los número menores a 5
# e imprima por consola [1, 3, 2]

nuevaTupla = list(tupla)
for numeros in nuevaTupla:
    if numeros < 5:
        print(numeros)

lista =[] #Definimos la lista
# Filtramos los elementos menores a 5 de la tupla
for elementos in tupla:
    if elementos < 5:
        lista.append(elementos)
print(lista)