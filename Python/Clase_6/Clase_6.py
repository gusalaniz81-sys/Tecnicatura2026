# En esta clase veremos la sentencia if/else
condicion = 'Hola alumnos'
if condicion == True:
    print("Condicion Verdadero")
elif condicion == False:
    print("Condicion Falso")
else:
    print("Condicion Falso")

condicion = False
if condicion:
    print("Condicion Verdadero")
else:
    print("Condicion Falso")

# Sintaxis simplificada con el operador ternario
print('Condicion Verdadera') if condicion else print('Condicion Falsa')
# Esta condicion se recomienda cuando la estructura es pequeña. (si o no)