#PRE: Vamos a tener una cadena de texto no vacia
SEPARADORES = ('.', ',', ';', ':', '"')
#texto = input("Introduce un texto sobre el que trabajar: ")
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis eu ipsum est. Sed varius lacus elit, at iaculis tellus elementum tempus. Proin dolor tellus, finibus ac elit quis, varius vulputate ex. Cras eu purus sed nunc lobortis congue. Mauris condimentum sem tincidunt auctor elementum. Morbi interdum nisi in porta lacinia. Proin eget turpis commodo, gravida diam id, varius turpis. Integer at est ut libero venenatis efficitur sed eu nibh. Pellentesque in ultricies eros, quis tincidunt arcu. Sed viverra tortor et risus dapibus rhoncus. Morbi fermentum, nulla a bibendum laoreet, tortor justo semper nisl, nec malesuada libero dolor at mauris.  Nulla ornare rutrum lorem, quis efficitur magna interdum nec. Morbi aliquet porta mi, sed rhoncus nisl luctus accumsan. Sed finibus hendrerit arcu. Phasellus fermentum, odio eget placerat scelerisque, ligula velit iaculis risus, vitae efficitur dui elit id nisi. Cras finibus est ut pretium fringilla. Cras facilisis orci mi, nec mollis enim finibus eu. Donec mi arcu, vulputate sed turpis in, posuere elementum tellus. Etiam hendrerit, lectus a tincidunt interdum, elit sapien vulputate mi, in ullamcorper nunc lacus at nisl. Nulla finibus feugiat vulputate. Proin nec erat lectus. Donec porttitor, metus non faucibus dapibus, diam leo mollis nisl, et euismod dolor metus et augue. Donec quis egestas nisi. Nulla ornare, ante ut hendrerit rhoncus, dui sapien consectetur velit, non posuere nisi urna nec metus. Cras vitae lorem pulvinar, porttitor mauris ultrices, gravida tortor.  Quisque ultricies neque at lorem vulputate, id pulvinar massa sollicitudin. Etiam ante elit, hendrerit non velit a, feugiat tempus libero. Etiam at orci at purus lacinia pharetra. Vestibulum vitae lobortis nulla, vitae facilisis orci. Cras consequat convallis velit sit amet gravida. Phasellus id dolor quis lectus sagittis faucibus id vel risus. Nullam eu orci quis felis sodales imperdiet mattis et ligula. Vestibulum ac sapien eget neque condimentum imperdiet. Phasellus eu urna eget eros mollis facilisis."

#1. Calcular frecuencia de palabras.
#1.1. Para calcular las palabras hay que separar el texto en palabras.
#1.1.1. Para separar las palabras usamos los espacios en blanco.
#1.1.1.1. Las palabras aisladas pueden tener signos de puntuacion.

for caracter in SEPARADORES:
    texto = texto.replace(caracter, '')

palabras = texto.split()

palabras_sin_repetir = set(palabras)

lista_palabras = []
for palabra in palabras_sin_repetir:
    lista_palabras.append((palabra, palabras.count(palabra)))

longitud_lista = len(lista_palabras)
for i in range(longitud_lista):
    for j in range(longitud_lista - i - 1):
        if lista_palabras[j][1] < lista_palabras[j+1][1]:
            lista_palabras[j],lista_palabras[j+1] = lista_palabras[j+1],lista_palabras[j]

for palabra in lista_palabras:
    print("Palabra:", palabra[0], "Longitud:", palabra[1])

#Como se calcula la media?
#Sumamos todas las longitudes del palabras del texto y las dividimos entre el numero de palabras
total = 0
for palabra in palabras:
    total += len(palabra)

print(total/len(palabras))

#POST: Calcular y mostrar la longitud media de las palabras,
# mostrar listado de palabras ordenadas de forma descendente
# por frecuencia.