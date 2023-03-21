"""a) Se guardan en un arreglo A 10 números pares.
b) Se guardan en un arreglo B 5 números impares.
c) Mostrar los elementos de cada arreglo.
d) Hallar el máximo del arreglo A.
e) Hallar el mínimo del arreglo B.
f) Obtener un arreglo C con los elementos de A seguidos de los elementos de B.
g) Obtener un arreglo D con los elementos de A multiplicados por 4."""

pares = []
impares = []
max_pares = 0
arr_c = []
arr_d = []

# Ingreso de números pares
print('Ingrese 10 números pares')

while len(pares) < 10:
    nump = int(input('Digite su número: '))
    if nump % 2 == 0:
        pares.append(nump)
    else:
        print('El número ingresado no es par')

# Ingreso de números impares
print('Ingrese 5 números impares')

while len(impares) < 5:
    nump = int(input('Digite su número: '))
    if nump % 2 != 0:
        impares.append(nump)
    else:
        print('El número ingresado no es impar')

# Se declara variable de min impares
min_impares = impares[0]

# Maximo del primer arreglo
for i in pares:
    if i > max_pares:
        max_pares = i

# Maximo del segundo arreglo
for n in impares:
    if n < min_impares:
        min_impares = n

# Arreglo C
for c in pares:
    arr_c.append(c)
for e in impares:
    arr_c.append(e)

# Arreglo D
for u in pares:
    multi = u * 4
    arr_d.append(multi)

# Resultados solicitados

print(pares)
print(impares)
print(max_pares)
print(min_impares)
print(arr_c)
print(arr_d)
