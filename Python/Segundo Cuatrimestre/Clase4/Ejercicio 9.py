# Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
# Hacer un programa donde el usuario ingrese una frase, se le
# devolverá la misma frase pero sin espacios en blanco, y
# además un contador de cuántos caracteres tiene la frase
# (sin contar los espacios en blanco)
# Ejemplo:      Frase == vivir por siempre en paz
#               frase final: vivirporsiempreenpaz
#               N° de caracteres = 20

frase = input("Introduce tu frase: ")
frase_sin_espacios = frase.replace(" ", "")
print(frase_sin_espacios)
print(len(frase_sin_espacios))

frase2 = input("Introduce tu frase: ")
frase3 = " "
for i in frase2:
    if i != " ":
        frase3 += i
frase2 = frase3
print(f'\nLa frase es: {frase2}')
print(f'N° Caracteres: {len(frase2)}')