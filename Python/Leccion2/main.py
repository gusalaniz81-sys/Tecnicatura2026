#En esta clase veremos la sentencia if/else

##condicion = True
#if condicion:
#    print('Condicion Verdadera')
#else:
#    print('Condicion Falso')

#condicion1 = ''
#if condicion1:
#    print('Condicion Verdadera')
#else:
#    print('Condicion Falso')

'''condicion2 = 10
if condicion2 == True:
    print('Condicion Verdadera')
elif condicion2 == False:
    print('Condicion Falso')
else:
    print('Condicion sin especificar')'''
from pyexpat.errors import messages

'''
num = int(input('Ingrese un numero en el rango del 1 al 3: '))
numTexto = ''
if num == 1:
    numTexto = 'Número 1'
elif num == 2:
    numTexto = 'Numero 2'
elif num == 3:
    numTexto = 'Numero 3'
else:
    numTexto = 'Has introducido un numero fuera del rango'
print(f'El número ingresado es: {num} - {numTexto}')
'''
'''
#Ejercicio: Valor dentro de un rango
valor = int(input('Ingrese un numero entre 1 al 5: '))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valor >= valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f'El valor {valor} está dentro del rango')
else:
    print(f'El valor {valor} NO está dentro del rango')
    '''
"""
#Ejercicio con el operador OR
vacaciones = False
diaDescanso = True
if vacaciones or diaDescanso:
    print('Puede asistir al juego')
else:
    print('Tiene trabajo que hacer')

#Ejercicio con el operador OR, Operador not
vacaciones = False
diaDescanso = False
if not (vacaciones or diaDescanso):
    print('Puede asistir al juego')
else:
    print('Tiene trabajo que hacer')
"""
"""
#Ejercicio: Rango entre 20 y 30 años
edad = int(input('Ingrese su edad: '))
veinte = edad >= 20 and edad < 30
print(veinte)
treinta = edad >= 30 and edad < 40
print(treinta)
"""
"""
if veinte or treinta:
    print("Estás dentro del rango de los (20\'0) a (30\'0) años")
else:
    print("No estás dentro del rango de los (20\'0) a (30\'0) años")
"""
"""
##Otras formas para realizar el ejercico
--1--
if veinte:
    print("Estás dentro del rango de los (20\'0) años")
elif treinta:
    print("Estás dentro del rango de los (30\'0) años")
else:
    print("No estás dentro del rango de los (20\'0) a (30\'0) años")
    
--2--
if veinte or treinta:
    if veinte:
        print("Estás dentro del rando de los (20\'0) años")
    elif treinta:
        print("Estás dentro del rando de los (30\'0) años")
    else:
        print(("No estás dentro del rango de los (20\'0) a (30\'0) años")
else:
    print("No estás dentro del rango de los (20\'0) a (30\'0) años")
    
--3--
edad = int(input('Ingrese su edad: '))
if(edad >= 20 and edad <= 30) or (edad >= 30 and edad < 40):
else:
    print("No estás dentro del rango de los (20\'0) a (30\'0) años")
    
--4--Sintaxis simplificada del operador AND
edad = int(input('Ingrese su edad: '))
if(20<=edad<30) or (30<=edad<40):
else:
     print("No estás dentro del rango de los (20\'0) a (30\'0) años")
"""
"""
numero1 = int(input('Ingrese valor para numero1: '))
numero2 = int(input('Ingrese valor para numero2: '))

if numero1 > numero2:
    print("El numero 1 es mayor")
else:
    print("El numero 2 es mayor")
"""

#Ejercicio: Tienda de libros
'''
print('Digite los siguiente datos del libro')
nombre = input('Ingrese el nombre del libro: ')
id = int(input('Ingrese el id del libro: '))
precio = float(input('Ingrese el precio del libro: '))
envioGratis = input('Indicar si el envio Gratis del libro (True/False): ')
if envioGratis == 'True':
    envioGratis = True
elif envioGratis == 'False':
    envioGratis = False
else:
    envioGratis = ('El valor es incorrecto, debe ingresa True/False')
print(f'''

''')
'''
'''
read = 5
unread = 4
if unread !=0:
    print(f"you have {unread} unread messages")
else:
    print(f"No unread messages. Check your {read} read messages")
'''
ID_name = "Kristen Steward"
voter_register_name = "Kristen Jaymes Steward"
valid_voter = ID_name == voter_register_name
print("Here's your ballot.")
print(valid_voter == True) #Igual
print("You must register to vote first.")
print(valid_voter != True) #Diferente
















