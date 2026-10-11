# Ejercicio 4: Calculadora de impuestos
# Crear una funció para calcular el total de un pago incluyendo
# un impuesto aplicable (iva)
# Formula: pago_total = pago_sin_impuestos + pago_sin_impuesto * (impuesto/100)
# Proporcione el pago sin impuesto: 1000
# Proporcione el monto del impuesto: 21%
# Pago con impuesto: xxxxx
impor_pago = int(input('Ingrese el importe de pago: '))
impuesto = int(input("Ingrese el impuesto: "))

def pago_con_iva(impor_pago, impuesto):
    pago_total = impor_pago + (impor_pago * impuesto) / 100
    return pago_total

resultado = pago_con_iva(impor_pago, impuesto)
print(f'El pago total con %{impuesto} de IVA es: {resultado}')