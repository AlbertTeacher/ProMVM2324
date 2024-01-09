#PRE: Vamos a tener una cadena de texto no vacia
SEPARADORES = ('.', ',', ';', ':', '"')
texto = input("Introduce un texto sobre el que trabajar: ")

#1. Calcular frecuencia de palabras.
#1.1. Para calcular las palabras hay que separar el texto en palabras.
#1.1.1. Para separar las palabras usamos los espacios en blanco.
#1.1.1.1. Las palabras aisladas pueden tener signos de puntuacion.

for caracter in SEPARADORES:
    texto = texto.replace(caracter, '')

palabras = texto.split()

palabras_sin_repetir = set(palabras)

#POST: Calcular y mostrar la longitud media de las palabras,
# mostrar listado de palabras ordenadas de forma descendente
# por frecuencia.