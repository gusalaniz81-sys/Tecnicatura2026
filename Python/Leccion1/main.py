"""
miVariable = 3
print(miVariable)
miVariable = "aa"
print(miVariable)
miVariable = 3.5
print(miVariable)

x = 10
y = 2
z = x + y
print(z)
# Las literales se escriben x240, la variable y=x984, la variable z = x304
print(id(x))
print(id(y))
print(id(z))

a = 10
print(type(a))

b = True
print(type(b))

# Tipos int, float, String, Boot
x = 10
print(x)
print(type(x))

x = 14.5
print(x)
print(type(x))
x = "Hola Mundo"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas (Sting)
miGrupoFaborito = "Queen"
print("Mi Grupo favorito es: "+ miGrupoFaborito)

miGrupoFaborito = "Queen"+" "+"La mejor banda"
print("Mi Grupo favorito es: "+ miGrupoFaborito)
caracteristica = "The best Rock Band"
print("Mi Grupo favorito es: "+ miGrupoFaborito +" "+ caracteristica)
print("Mi Grupo favorito es: ", miGrupoFaborito, caracteristica)

numero = "7"
numero2 = "8"
print(numero + numero2)
print(int(numero) + int(numero2))
numero3 = 7
numero4 = 8
print(numero3 + numero4)
#print(int(numero3) + int(numero4)

#Tpos Boleanos (boll)
miBoleano = True
print(miBoleano)
miBoleano = False
print(miBoleano)
miBoleano = 3<2
print(miBoleano)
miBoleano =3>2

miBoleano =4<2
print(miBoleano)

if miBoleano:
    print("El resultado es verdero")
else:
    print("El resultado es falso")

miBoleano2 = 4 > 2
print(miBoleano2)

if miBoleano2:
     print("El resultado es verdero")
else:
    print("El resultado es falso")

#Procesar la entrada del usuario
# Funcion --> input()
#resultado = input()
#print(resultado)
resultado = input("Ingrese un número: ") #Regresa un dato tipo String
print(resultado)
numero1 = input("Escribe el 1er número: ")
numero2 = input("escibe el 2do número: ")
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)
 """
'''
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
#print("resultado de la suma: ",suma)
print(f"resultado de la resta: {suma}")

resta = operandoA - operandoB
print(f"resultado de la resta: {resta}")

miltiplicacion = operandoA * operandoB
print(f"resultado de la multiplicacion: {miltiplicacion}")

division = operandoA / operandoB
print(f"resultado de la division: {division}")
print(f"El resultado de la division (int) es: {division}")

exponente = operandoA ** operandoB
print(f"resultado de la exponente: {exponente}")    
'''

''' EJERCICIO RECTANGULO:
alto = int(input('Proporciona el alto del rectangulo: '))
ancho = int(input('Proporciona el ancho del rectangulo: '))
area = alto * ancho
perimetro = (alto + ancho)/2
print('Perímetro: ',perimetro)
print('Area: ',area)
'''
"""
miVariable3 = 10
print(miVariable3)

#Operadores de reasignación
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 +=1
print(miVariable3)

# miVariable3 = miVariable -2
miVariable3 -=2
print(miVariable3)

# miVariable3 = miVariable *3
miVariable3 *=3
print(miVariable3)

# miVariable3 = miVariable /2
miVariable3 /= 2
print(miVariable3)
"""
d = 4
b = 2
resultado = d == b #Comprobamos si son iguales
print(resultado)

# Operador diferente
resultado = d != b
print(resultado)

#Operador mayor que
resultado = d > b
print(resultado)

# Operador Menor que
resultado = d < b
print(resultado)

# Operador mayor o igual que
resultado = d >= b
print(resultado)

"""
a = int(input('Introduce un numero: '))
print(f"El residuo de la  división es: {a%2}")
if a % 2 == 0:
    print("El valor de a es: {a} es un numero PAR")
else:
    print("El valor de a es: {a} es un numero impar")
"""
"""
edadAdulto = 18
edadPersona = int(input('Ingrese su edad: '))
if edadPersona >= edadAdulto:
    print(f'Su edad: {edadPersona} años, usted es mayor de edad')
else:
    print(f'Su edad es: {edadPersona} años, usted es menor de edad')

miVariable = 10
print(miVariable)
miVariable = miVariable + 1
print(miVariable)
miVariable +=1
print(miVariable)
miVariable -=2
print(miVariable)
miVariable2 = 10
#miVariable2 = miVariable2 * 3
miVariable2 *= 3
print(miVariable2)

miVariable3 =12
miVariable3 = miVariable3 / 2
#miVariable3 /= 2
print(miVariable3)
"""