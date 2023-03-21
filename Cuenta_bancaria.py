""" Se ingresa el nombre y apellido, el saldo de la caja de ahorro y el saldo de la caja de cuenta corriente de los clientes de un banco hasta que el nombre y apellido sea FIN. Calcular y mostrar:

Nombre y apellido del cliente que tiene el mayor saldo en la caja de ahorro
Cantidad de clientes cuyo saldo en caja de ahorro o en cuenta corriente sea negativo.
Total de dinero depositado en ambas cajas.
Mostrar el nombre y apellido de aquellos clientes que no tienen dinero en ambas cuentas.
"""

Nombre = input('Ingrese el nombre: ')
Nombre = Nombre.lower()
Apellido = input('Ingrese el apellido: ')
Apellido = Apellido.lower()
caja_ahorro = 0
cuenta_corriente = 0
cuentas_negativas = 0
clientes_sin_dinero = ' '
cliente_mas_ahorro = ' '
ahorro_mayor = 0

while Nombre != 'fin' and Apellido != 'fin':
    saldo_corriente = input('Ingrese el saldo de su cuenta corriente')
    cuenta_corriente = int(saldo_corriente)
    saldo_ahorro = input('Ingrese el saldo de su caja de ahorro')
    caja_ahorro = int(saldo_ahorro)

    if caja_ahorro > ahorro_mayor:
        cliente_mas_ahorro = f'{Nombre} {Apellido}'

    if caja_ahorro < 0:
        cuentas_negativas = cuentas_negativas + 1
    elif cuenta_corriente < 0:
        cuentas_negativas = cuentas_negativas + 1
    else:
        pass

    total_dinero = cuenta_corriente + caja_ahorro
    print(f'El total depositado por este cliente es de {total_dinero}$')

    if cuenta_corriente == 0 and caja_ahorro == 0:
        print(f'el cliente {Nombre} {Apellido}, no tiene dinero en el banco')

    Nombre = input('Ingrese el nombre: ')
    Nombre = Nombre.lower()
    Apellido = input('Ingrese el apellido: ')
    Apellido = Apellido.lower()

print(f'El cliente que mas saldo tiene en la caja de ahorro es {cliente_mas_ahorro}')
print(f'Hay {cuentas_negativas} clientes que no tienen saldo negativo')
