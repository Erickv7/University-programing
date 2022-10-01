# Categorias de empleados
# Conteo total
Sueldos_pagados = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0

# Calculo de Sueldos
# Ingrese la cantidad de empleados a pagar
emp = int(input('Dime el número de empleados'))
# Calculo de sueldo según categoría

while emp > 0:
    horas = int(input('Ingrese la cantidad de horas trabajadas '))
    cat = int(input('Ingrese la categoría de este empleado '))
    sueldo_bruto = 0
    sueldo_neto = 0
    emp = emp - 1

    if cat == 1:
        sueldo_bruto = 150 * horas
        descuentos = sueldo_bruto / 100 * 17
        sueldo_neto = sueldo_bruto - descuentos
        c1 = c1+1
        Sueldos_pagados = Sueldos_pagados + sueldo_bruto
        print(f'El sueldo de este mes de este empleado es de {sueldo_neto}$')

    elif cat == 2:
        sueldo_bruto = 200 * horas
        descuentos = sueldo_bruto / 100 * 17
        sueldo_neto = sueldo_bruto - descuentos
        c2 = c2+1
        Sueldos_pagados = Sueldos_pagados + sueldo_bruto
        print(f'El sueldo de este mes de este empleado es de {sueldo_neto}$')
    
    elif cat == 3:
        sueldo_bruto = 250 * horas
        descuentos = sueldo_bruto / 100 * 17
        sueldo_neto = sueldo_bruto - descuentos
        c3 = c3+1
        Sueldos_pagados = Sueldos_pagados + sueldo_bruto
        print(f'El sueldo de este mes de este empleado es de {sueldo_neto}$')
    
    elif cat == 4:
        sueldo_bruto = 280 * horas
        descuentos = sueldo_bruto / 100 * 17
        sueldo_neto = sueldo_bruto - descuentos
        c3 = c4+1
        Sueldos_pagados = Sueldos_pagados + sueldo_bruto
        print(f'El sueldo de este mes de este empleado es de {sueldo_neto}$')

    else:
        print('La categoría ingresada en incorrecta')

# Entrega de resultados obtenidos
print(f'El total de sueldo pagado en la empresa es de {Sueldos_pagados}')
print(f'La cantidad de empleados en la categoría 1 es de {c1}\n La cantidad de empleados en la categoría 2 es de {c2}\n La cantidad de empleados en la categoría 3 es de {c3}\n La cantidad de empleados en la categoría 4 es de {c4}\n')
