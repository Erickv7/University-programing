"""
En base a los conceptos vistos en el módulo, debés realizar el siguiente ejercicio:
Ingresar números enteros hasta que sea dicho número cero y cargar un arreglo con aquellos
números múltiplos de 5. Mostrar el arreglo y calcular:
a. Los 3 primeros números más grandes.
b. Generar otro arreglo con los números múltiplos de 10. Si no los hubiera mostrar una leyenda.
c. Eliminar del arreglo original el valor mínimo. Si los hubiera repetido,
eliminar todas las apariciones del elemento mínimo
"""

# Se crea el arreglo y se cargan los números
Arr = []
numero = int(input('Ingrese el primer número: '))

while numero != 0:
    numero = int(input('Ingrese otro número: '))
    if numero == 0:
        pass
    elif numero % 5 == 0:
        Arr.append(numero)


# Se muestra arreglo
print(Arr)

# Se muestran los digitos mayores
Arr.sort()
print(Arr[-1], Arr[-2], Arr[-3])

# Se muestra arreglo con multiplos 10
Arr2 = [0]
for i in Arr:
    if i % 10 == 0:
        Arr2.append(i)

if Arr2 == 0:
    Arr2.pop(0)
    print('No se encontraron multiplos de 10')
else:
    Arr2.pop(0)
    print(Arr2)

# Eliminar el número menor del arreglo
eliminar = Arr[0]
Arr.remove(eliminar)
print(Arr)
