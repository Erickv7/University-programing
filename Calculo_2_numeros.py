# Ejercicio Modulo 4
'''En base a los conceptos vistos en el módulo, debés realizar el siguiente ejercicio:

Diseñar un programa en Python que permita:

 Ingresar dos números y mostrar con el mensaje correspondiente:

La suma.
La diferencia.
El producto.
El resultado de elevar el primero al segundo.'''

# Ingresar el número
numero = int(input('Ingrese un número'))
numero2 = int(input('Ingrese otro número'))

# Se realizan las operaciones correspondientes
suma = numero + numero2
difernecia = numero - numero2
if difernecia < 0:
    difernecia = difernecia*-1
producto = numero / numero2
elevar = numero**numero2

# Se muestran los resultados
print(f'La suma de tus números es {suma}')
print(f'La diferencia entre tus números es {difernecia}')
print(f'el producto de tus números es {producto}')
print(f'El resultado de elevar al número es {elevar}')
