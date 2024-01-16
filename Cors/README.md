# Kata (Python) - Cors (Joc de cartes)

El vostre objectiu és avaluar una sola mà de cors i determinar la carta guanyadora. Seguiu aquest enllaç (https://gamerules.com/rules/hearts-card-game/) per obtenir regles més detallades, però les regles bàsiques són les següents.

No hi ha cartes "trump" als cors. Això vol dir que la primera carta jugada sempre guanyarà la mà si és l'única carta d'aquest pal.

I.E.: Si l'Àlex juga al dos de les maces "2C" Bob juga al tres de piques "3S" Chris juga al rei dels diamants "KD" i Dave juga al dos de cors "2H" Alex guanya aquesta mà.

Els valors de les cartes són 2 com a carta més baixa i l'As com a carta més alta, seguint l'ordre típic de la baralla de cartes. No es donaran targetes duplicades.

El valor de retorn d'aquesta funció hauria de ser la targeta guanyadora com a cadena, sensible a majúscules i minúscules

No hi ha altres regles importants que s'hagin de seguir. En altres paraules, no importa si aquesta és la primera mà o l'última mà. L'únic que importa és el valor de la carta més alta respecte a les altres regles. Això només és per a un joc de cors de 4 jugadors. No cal provar més o menys jugadors.

Aquests són alguns exemples del que faria un codi d'èxit. Consulteu altres casos de prova per obtenir proves més aprofundides. S'utilitzarà un conjunt de 50 proves aleatòries abans de poder enviar-les.

  "La mà jugada (entrada): ['10C', 'JC','AC', 'QC'] Tothom ha jugat amb vestit, de manera que la carta més alta d'aquest set guanya. La sortida hauria de ser: "AC"

La mà jugada (entrada): ['4C', 'KH', 'QS', '10D'] Alex va liderar amb maces. Ningú més va jugar a clubs, així que l'Àlex guanya aquesta mà tot i que la carta de tots els altres és més alta. La sortida hauria de ser: '4C'

La mà jugada (entrada): ['9D', '9C', 'QD', '9S'] Només l'Alex i el Chris van jugar amb vestit. De les dues cartes que tenen el joc, la carta de Chris té un valor més alt. La sortida hauria de ser: 'QD'."