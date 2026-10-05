#Ejercicio 6: Tabla de multiplicar
# Hacer un programa que pida un número por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10.
# Por ejemplo: Si ingresamos el 5, la lista tendrá: 5,10,15,20,25,30,35,40,45,50

tabla = []
num = int(input('Ingrese un numero: '))
for i in range(1,11):
    resultado = num * i
    tabla.append(resultado)
print(tabla)


