'''
 Hem de tenir 52 cartes a repartir
 4 jugadors que tindran 13 cartes repartides de forma aleatoria
 El jugadors jugaran fins que es quedin sense cartes
 Qui guanya la ma? Qui treu la carta mes alta del pal inicial
 Com comptem els punts? 1 punt per cada cor, 13 per QS
 Guanya qui tingui MENYS punts
 Quins pals hi ha? H, C, D, S
 Cartes? 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
'''
# Creamos lista de cartas
cards = []
for suit in ['H', 'C', 'D', 'S']:
    for num in range(2, 11):
        cards.append({'suit': suit, 'num': num, 'value': num, 'name': ''.join([str(num), suit])})
    cards.append({'suit': suit, 'num': 'J', 'value': 11, 'name': ''.join(['J', suit])})
    cards.append({'suit': suit, 'num': 'Q', 'value': 12, 'name': ''.join(['Q', suit])})
    cards.append({'suit': suit, 'num': 'K', 'value': 13, 'name': ''.join(['K', suit])})
    cards.append({'suit': suit, 'num': 'A', 'value': 14, 'name': ''.join(['A', suit])})

# Declaramos los jugadores
players = [[], [], [], []]

# Repartir las cartas
# Iniciamos la semilla del aleatorio
seed = 427

# Tenemos que repartir todas y cada una de las cartas a cada jugador
## Opcion 1: Repartir 13 cartas a un jugador, y repetir
## Opcion 3: Repartir 1 carta por jugador hasta que nos quedemos sin cartas
# Opcion 1
'''
for i in range(len(players)):
    for j in range(13):
        seed = (seed * 997) % 1000
        random = (seed * 503) % 1000 / 1000
        numero = int(random * len(cards))
        players[i].append(cards.pop(numero))
'''
# Opcion 2
i = 0
while len(cards) > 0:
    seed = (seed * 997) % 1000
    random = (seed * 503) % 1000 / 1000
    numero = int(random * len(cards))
    players[i % len(players)].append(cards.pop(numero))
    i += 1

# Jugar la partida
# Cada jugador jugara una carta

sin_cartas = False
for player in players:
    sin_cartas = (len(player) == 0) or sin_cartas

while sin_cartas == False:
    for i in len(players):
        ...