# Cadena de hoteles
"""
Este programa nos permite calcular en una cadena de 10 hoteles cual es el porcentaje de ocupación de cada uno, cual es la ciudad que
posee el hotel con mas habitaciones y también cual es la capacidad total de toda la cadena de hoteles.
"""

capacidad_total = 0
ciudad_mas_habitaciones = 0
max_habitaciones = 0

for i in range(1, 11):
    ciudad = input('Ingrese las ciudades donde hay hoteles ')

    # Capacidad total del hotel
    capacidad = input('ingrese la cantidad de huéspedes que puede alojar el hotel ')
    habitaciones = input('ingrese el númmero de habitaciones del hotel ')
    huespedes_mes = input('Número de huéspedes recibidos en un mes ')

    # Sumatoria de totales
    porcentaje = int(capacidad) / 100
    ocupacion = int(huespedes_mes) / int(porcentaje)
    capacidad_total = int(capacidad_total) + int(capacidad)
    print(f'La ocupación del hotel de {ciudad} es del {ocupacion}%')

    if int(habitaciones) > int(max_habitaciones):
        max_habitaciones = habitaciones
        ciudad_mas_habitaciones = ciudad
print(f'La cantidad de huéspedes que puede alojar la cadena es de {capacidad_total}')
print(f'El hotel con más cantidad de habitaciones es el hotel de {ciudad_mas_habitaciones}')
