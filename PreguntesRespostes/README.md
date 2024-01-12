# Preguntes i Respostes

Escriu un programa en Python3 que implementi un joc de preguntes i respostes.

Defineix una llista de preguntes amb les seves respostes associades.

El programa ha de fer el següent:

- Escull aleatòriament una pregunta de la llista i la mostra a l'usuari.*
- L'usuari ha de respondre a la pregunta.
- Verifica si la resposta de l'usuari és correcta i dóna una puntuació.
- Manté un recompte de la puntuació total de l'usuari.
- Repeteix el procés fins que l'usuari decideixi finalitzar el joc.

**Com fer un número aleatori?: crearem una variable anomenada seed i farem que tingui el valor que vulguis, llavors en el punt on vulguis fer servir un número aleatori farem el següent codi.
seed = (seed * 997) % 1000
random = (seed * 503) % 1000 / 100
numero_pregunta = int(random * (len(llista_preguntes)))*