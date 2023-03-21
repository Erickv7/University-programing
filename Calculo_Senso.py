# Programa para calcular parametros del senso buenos aires
# Parametros solicitados
edad = 1
estudio = 0
Fem = 0

# Niveles de estudio
est_primario = 0
edad_primario = 0
est_secundario = 0
edad_secundario = 0
est_terciario = 0
edad_terciario = 0

# Otros parametro solicitados
Hom_may_45 = 0
Edad_estudios = 0
Mujeres_ter = 0
Hom_30_ter = 0
Fem_40_sec = 0
edad_fem_40_sec = 0

# Ingreso de información para el censo

while edad > 0:
    ed = input('Ingrese su edad')
    edad = int(ed)
    gen = input('Marque 1 para Femenino y 2 para Masculino')
    if gen == 1:
        Fem = Fem + 1

    est = input('Ingrese el nivel de estudios alcanzado, sea primario, secundario o terciario')
    estudio = int(est)
    if estudio == 1:
        edad_primario = edad_primario + int(edad)
        est_primario = est_primario + 1
    elif estudio == 2:
        edad_secundario = edad_secundario + int(edad)
        est_secundario = est_secundario + 1
    elif estudio == 3:
        edad_terciario = edad_terciario + int(edad)
        est_terciario = est_terciario + 1
    else:
        print('El parametro ingresado es incorrecto')

    if gen == 2 & int(edad) > 45:
        Hom_may_45 = Hom_may_45 + 1
    elif gen == 1 & int(estudio) == 3:
        Mujeres_ter = Mujeres_ter + 1
    elif gen == 2 & int(edad) > 30 & int(estudio) == 3:
        Hom_30_ter = Hom_30_ter + 1
    elif gen == 1 & int(edad) > 40 & int(estudio) == 2:
        Fem_40_sec = Fem_40_sec + 1
        edad_fem_40_sec = edad_fem_40_sec + int(edad)
    else:
        pass

# Promedios

Edad_mujeres_secundario = 0
promedio_primario = 0
promedio_secundario = 0
promedio_terciario = 0

if est_primario > 0:
    promedio_primario = edad_primario / est_primario
else:
    pass

if est_secundario > 0:
    promedio_secundario = edad_secundario / est_secundario
else:
    pass

if est_terciario > 0:
    promedio_terciario = edad_terciario / est_terciario
else:
    pass

if Fem_40_sec > 0:
    Edad_mujeres_secundario = edad_fem_40_sec / Fem_40_sec
else:
    pass


print(f'La cantidad de hombres mayores de 45 años es {Hom_may_45}')
print(f'La cantidad de mujeres encuestadas es de {Fem}')
print(f'Promedio de edad para personas con estudios primarios {promedio_primario}')
print(f'Promedio de edad para personas con estudios secundarios {promedio_secundario}')
print(f'Promedio de edad para personas con estudios terciarios {promedio_terciario}')
print(f'El pocentaje de hombres mayores de 30 y con estudios terciarios es de {Hom_30_ter}')
print(f'Las edad promedio de las mayores de 40 con secundarios es de {Edad_mujeres_secundario}')
