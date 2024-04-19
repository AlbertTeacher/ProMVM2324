llista_preguntes = (('2+2? ', '4'), ('3+2? ', '5'), ('4+2? ', '6'), ('5+2? ', '7'))

end = 'n'
puntos = 0

seed = int(input("Introdueix un nombre major de 0: "))

while end == 'n':
    seed = (seed * 997) % 1000
    random = (seed * 503) % 1000 / 1000
    numero_pregunta = int(random * (len(llista_preguntes)))

    respuesta = input(llista_preguntes[numero_pregunta][0])

    puntos += 1 if respuesta == llista_preguntes[numero_pregunta][1] else 0;
    
    end = input('Quieres salir? [s/n] ')

print("Puntos totales:", puntos)