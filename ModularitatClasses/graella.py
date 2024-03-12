class Coordenada:
    def __init__(self):
        # Coordenada inicial
        self.x: int = 0
        self.y: int = 0

    def moure_dreta(self):
        self.x += 1

    def moure_esquerra(self):
        self.x -= 1

    def moure_amunt(self):
        self.y += 1

    def moure_avall(self):
        self.y -= 1

class Main:
    # Programa principal
    def __init__(self):
        # Executar moviments
        coordenada: Coordenada = Coordenada()
        coordenada.moure_dreta()
        print(f"Nova coordenada després de moure a la dreta: ({coordenada.x}, {coordenada.y})")

        coordenada.moure_amunt()
        print(f"Nova coordenada després de moure amunt: ({coordenada.x}, {coordenada.y})")

Main()
