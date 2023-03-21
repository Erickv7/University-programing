"""
Cargar un arreglo con 12 números enteros. Mostrarlo y calcular:

El elemento máximo y mínimo.
Calcular el promedio de los elementos ubicados en posiciones pares.
Insertar después del elemento máximo, la mitad del mismo.
Mostrar el arreglo ordenado de mayor a menor.
"""

# Se carga el arreglo en en programa y se muestra por pantalla
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(arr)

# Calculo de promerio de posiciones pares en el arreglo
promedio = arr[2:12:2]
divisor = len(promedio)
suma_promedio = sum(promedio)
prom = suma_promedio / divisor
print(prom)

# Calculos de maximos y minimos del arreglo
maximo = 0
minimo = 1000

for i in arr:
    if i > maximo:
        maximo = i

for i in arr:
    if i < minimo:
        minimo = i

# Se muestan en pantalla los maximos y minimos
print(maximo)
print(minimo)

# Se agrega a la lista la mitad del número mayor y se muestra por pantalla
arr.append(maximo/2)
print(arr)

# Se ordena de mayor a menor la lista y se muestra en pantalla
arr.sort()
arr.reverse()
print(arr)
