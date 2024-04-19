'''
1. Gestionar reparacio cotxe
2.1. Introduir quines peces son necessaries
2.2. Reparar cotxe
3.1.1. Demanar per teclat quines peces son necessaries
3.2.1. Comprovar si tenim les peces
3.2.2. Si no tenim demanar
3.2.3. Si tenim reparar
'''
def demanar_peces():
    print("hola")

class Taller:
    def __init__(self):
        self.stock : list(str) = ["rodes", "oli", "motor"]

    def exec(self) -> None:
        pieces = self.demanar_peces()
        self.reparar_cotxe(pieces)

    def demanar_peces(self) -> str:
        pieces = input("Que necessitem per reparar el cotxe: ")

        return pieces

    def reparar_cotxe(self, pieces: str) -> None:
        pieces_exists = self.check_pieces(pieces)

        if pieces_exists:
            self.stock.remove(pieces)
            self.informar_cotxe_reparat()
        else:
            self.renovar_stock(pieces)

    def check_pieces(self, pieces: str) -> bool:
        return pieces in self.stock

    def renovar_stock(self, pieces:str) -> None:
        print(f"S'ha demanat per renovar stock de {pieces}")

    def informar_cotxe_reparat(self) -> None:
        print("El cotxe s'ha reparat")


app = Taller()
app.exec()
