class Carrito:
    '''
    1. Gestionar carrito de compra
    2.1. Anyadir productos al carrito
    2.2. Eliminar productos del carrito
    2.3. Eliminar linea de compra
    2.4. Calcular importe
    '''
    def __init__(self):
        self.carrito = dict()
    def add_product(self, product: str, qty: int) -> None:
        '''
        Si producto existe en el diccionario, sumar qty
        Si no existe add
        '''
        if product in self.carrito.keys():
            self.carrito[product] += qty
        else:
            self.carrito[product] = qty

    def decrement_product(self, product: str) -> None:
        if product in self.carrito.keys():
            self.carrito[product] -= 1
            if self.carrit[product] =< 0:
                self.delete_line(product)
    def delete_line(self, product: str) -> None:
        if product in self.carrito.keys():
            self.carrito.delete(product)
    def calculate_total(self) -> int:
        ...
