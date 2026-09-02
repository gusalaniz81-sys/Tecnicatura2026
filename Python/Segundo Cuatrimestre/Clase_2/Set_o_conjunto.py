# Tipo set
planetas ={'Marte', 'Júpiter', 'Venus'}
print(planetas)
print(len(planetas)) #Usamos la función len = length significa largo

#Revisar si un elemento existe dentro del set
print('Marte' in planetas)
print('Jupiter' in planetas)

#Agregar un elemento
planetas.add('Tierra') #add es una función
planetas.add('Tierra')
print(planetas)

#Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Tierra') #Esta función ante un mal ingreso u inexistencia del elemento da error
print(planetas)
planetas.discard('Jupiter') # Esta fuunción no nos presenta ningún error
print(planetas)

#LImpiar set
planetas.clear()
print(planetas)

#Eliminar set o conjunto
del planetas
print(planetas) #Al eliminar nos muestra un error