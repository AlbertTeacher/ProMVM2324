class Libro:
    def __init__(self, titulo: str, autor: str, cantidad: int):
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad

    def prestar(self) -> None:
        if self.cantidad > 0:
            self.cantidad -= 1
            print(f"Libro prestado: {self.titulo}, autor: {self.autor}")
        else:
            print(f"No hay ejemplares de {self.titulo}")

    def devolver(self) -> None:
        self.cantidad += 1
        print(f"Libro devuelto: {self.titulo}, autor: {self.autor}")

    def informacion(self) -> None:
        print(f"titulo: {self.titulo}, autor: {self.autor}, ejemplares disponibles: {self.cantidad}")
