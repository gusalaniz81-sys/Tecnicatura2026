### Ejercicio: Tienda de libros###

print('Ingrese los siguientes datos: ')
nombre = input('Ingrese el nombre del libro: ')
id = int(input('Ingrese el ID del libro: '))
precio = float(input('Ingrese el precio del libro: '))
envioGratis = input('Ingrese si el envio es gratuito (True/False: ')
if envioGratis == 'True':
    envioGratis = True
elif envioGratis == 'False':
    envioGratis = False
else:
    envioGratis = 'El valor es incorrecto, debe escribir True/False'
print(f'''
        nombre: {nombre}
        id: {id}
        precio: {precio}
        envioGratis: {envioGratis}
''')