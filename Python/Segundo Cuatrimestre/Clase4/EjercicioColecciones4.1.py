# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuacion
# elimine los elementos repetidos, por ultimo mostara la lista

# Creamos una lista
lista = [1, 2, 3, "Lisandro", 5, 5, 4, "Basty", 6, "Yamila"]
#conjunto = set(lista) #Convertimos la lista a un conjunto de tipo set
#lista = list(conjunto) # Convertimos el conjunto a una lista
lista = list(set(lista)) #La conversión hecha en una sola linea de código (eficiente)
print(lista)
