# Ciclo while (minetras o durante)
contador = 0
while contador < 5:
    print('Ejecutar nuestro ciclo while ', contador)
    contador += 1
else:
    print('Finde ciclo while')

minimo = 1
contador = 5
while contador >= minimo:
    print(contador)
    contador -= 1

# Ciclo for
cadena = 'Hello'
for letra in cadena:
    print(letra)
else:
    print('Fin del ciclo for')

#Palabra reservada Break
for letra in 'Alemania':
    if letra == 'a':
        print(f'La letra encontrada: {letra}')
        break
else:
    print('Fin del ciclo for')

#Palabra reservada continue
for i in range(6):
    if i % 2 == 0:
        print(f'Valor: {i}')

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')