from carrito import Carrito

class Ferreteria:
    '''
    1. Gestionar compras en una ferreteria
    2.1. Gestionar carrito de compra
    2.2. Pagar compra
    3.1.1. Anyadir productos al carrito
    3.1.2. Eliminar productos del carrito
    3.2.1. Calcular importe
    3.2.2. Finalizar compra
    '''
    def __init__(self):
        self.carrito = Carrito()

    def add_product(self, product: str, qty: int) -> None:
        self.carrito.add_product(product, qty)

    def delete_product(self, product: str, qty: int) -> None:
        for i in range(qty):
            self.carrito.decrement_product(product)
    
    def calculate_total(self) -> None:
        print(self.carrito.calculate_total())
    
    def end_purchase(self) -> None:
        self.carrito.show_lines()
        self.carrito.pay()
    
app = Ferreteria()
app.add_product("cargol", 7)
app.calculate_total()
app.add_product("cargol", 3)
app.calculate_total()
app.add_product("martell", 1)
app.calculate_total()
app.delete_product("cargol", 2)
app.calculate_total()
app.end_purchase()
app.calculate_total()
app.add_product("cargol", 1)
app.calculate_total()
