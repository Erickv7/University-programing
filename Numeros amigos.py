"""
En base a los conceptos vistos en el módulo, debés realizar el siguiente ejercicio:
Dos números son amigos si cada uno de ellos es igual a la suma de los divisores del otro.
Por ejemplo, 220 y 284 son amigos ya que:
La suma de divisores de 284 es 1 + 2 + 4 + 71 + 142 = 220
La suma de divisores de 220 es:
1 + 2 + 4 + 5 + 10 + 11 + 20 +22 + 44 + 55 + 110 = 284
"""

# Ingreso de numeros
n1 = int(input('Ingresa el primer número: '))
n2 = int(input('Ingresa el segundo número: '))
divi = 1
suma_divi = 0

# Buscar el los divisores y sumarlo
while divi < n1:
    if n1 % divi == 0:
        suma = suma_divi + divi
    divi = divi + 1

# Comprobar si son números amigos
if suma_divi == n2:
    print('Los números son amigos')
else:
    print('Los números no son amigos')
