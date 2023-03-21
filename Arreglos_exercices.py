"""
 Ingresar un arreglo e imprimirlo. Se da como dato el número de componentes delvector
"""

"""Arr = []
for i in range(0, 10):
    ar = input('Ingrese los 10 elementos que tendra el arreglo: ')
    Arr.append(ar)

print(Arr)"""


"""
Ingresar un arreglo de 10 componentes:
a. Imprimir la cuarta componente.
b. Imprimir las componentes en orden invertida.
c. Imprimir el producto entre la primera y la última componente.
d. Imprimir las componentes de índice impar.
e. Imprimir la suma de las componentes de índice par.
f. Imprimir la multiplicación de las componentes de índice impar.
g. Imprimir el arreglo que resulta de intercambiar la primera con la última componente
"""

Arr = []

# Ingresar los elementos necesarios para el arreglo
for i in range(0, 10):
    ar = int(input('Ingrese los 10 elementos que tendra el arreglo: '))
    Arr.append(ar)

# F multiplicar los componenetes de índice impar
Arr2 = Arr[1:9:2]
multi = 0
for n in Arr2:
    multi = multi * n

print(Arr[3])
print(Arr.reverse())
print(Arr[1:9])
print(Arr[1:9:2])
print(sum(Arr[0:10:2]))
print(multi)
