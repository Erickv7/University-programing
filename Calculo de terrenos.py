"""a) Cargar un arreglo de 15 elementos con las medidas del ancho de 15 terrenosrectangulares.
b) Cargar otro arreglo de 15 elementos con las medidas del fondo de los terrenos.
c) Hallar el arreglo superficie. Mostrarlo ordenado.
d) Hallar cuál es el ancho correspondiente al terreno de mayor fondo."""

# Cargar las medidas en el arreglo

anc = []
lar = []
terreno = []
mas_profundo = 0

# Ingreso de medidas
for i in range(0, 2):
    ancho = int(input('Ingrese el ancho del terreno: '))
    anc.append(ancho)

for n in range(0, 2):
    largo = int(input('Ingrese el largo del terreno: '))
    lar.append(largo)

# Calculo del terreno mas profundo
for e in lar:
    if e > mas_profundo:
        mas_profundo = e

# Calcular el area de los terrenos
def sumar():
    for a in range(len(anc)):
        terreno.append(lar[n] + anc[i])
    return

# Mostrar resultados

sumar()

print(terreno)
print(mas_profundo)
