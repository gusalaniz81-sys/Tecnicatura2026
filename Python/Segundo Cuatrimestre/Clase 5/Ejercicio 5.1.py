# Ejercicio 10: No repetir caracteres
# Hacer un programa que pida una cadena por teclado, luego
# meter los carácteres en una lista sin repetir caracteres

caracteres = []
cadena = input("Ingresar una cadena: ")
for i in cadena:
    if i not in caracteres:
        caracteres.append(i)
print(caracteres)
