"""
Diseñar un programa en Python que permita:
Ingresar una cadena de caracteres y:

Mostrar con qué letra empieza.
Mostrar con qué letra termina.
Mostrar cuántas letras tiene.
Mostrar toda la cadena en mayúsculas.
Reemplazar los blancos de la cadena por '**' y mostrar la cadena de caracteres.
Mostrar la cadena invertida.
"""

texto = input('Ingrese su texto: ')

# Extracción de parametros solicitados

Primera_letra = texto[0]
Letra_final = texto[-1]
if Letra_final == '.':
    Letra_final = texto[-2]

Largo_texto = len(texto)
cadena_mayuscula = texto.upper()
texto_espacios = texto.replace(' ', '**')
texto_invertido = texto[::-1]

print(f'La cadena empieza con: {Primera_letra}')
print(f'La cadena termina con: {Letra_final}')
print(f'El largo de la cadena es de: {Largo_texto}')
print(f'La cadena en masyúsculas: {cadena_mayuscula}')
print(f'El texto sin espacios y con **: {texto_espacios}')
print(f'El texto invertido: {texto_invertido}')
