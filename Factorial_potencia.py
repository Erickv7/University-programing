# Ejercicios de 100 números
""" Este programa nos permite realizar operaciones con los número que hay del 1 al 100, permitiendonos elegir que operación
    queremos realizar entre las que tenemos obtener el factorial de un número, su potencia o saber si es un número par o impar.
"""

numeros = list(range(1, 101))

for i in numeros:
    print('\nQue deseas hacer con este numero \n Si deseas el factorial ingresa "1" \n Si deseas la potencia ingresa 2 '
          '\n Si no ingresa 3 y te diremos si el valor es par, impar o nulo')

    op = int(input('Por favor ingrese un número '))
    if op == 1:
        resp = 0
        for n in range(0, i):
            resp = resp * n

        print(f'El factorial de tu número es {resp}')

    elif op == 2:
        pot = int(input('Por favor ingrese el número al que desea potenciar'))
        potencia = i ** pot
        print(f'La potencia de tu número es {potencia}')

    elif op == 3:
        resto = i % 2
        if resto == 1:
            print('Tu número es impar')
        else:
            print('Tu número es par')
    else:
        print('El valor seleccionado no es correcto')
