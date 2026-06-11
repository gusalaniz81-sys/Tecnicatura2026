'''
Ejercicio: Determinar la solucion de la siguiente
if expresion is None:
    ((3+5*8)<3 and ((-6/3*4)+2<2) or (a>b))
1. Pedir al usuario los dos valores para a y b
2: Escribir en código la siguiente expresion
3. Mostrar el resultado
'''
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
resultado = ((3+5*8)<3 and ((-6/3*4)+2<2) or (a>b))
print(f'El resultado es : {resultado}')