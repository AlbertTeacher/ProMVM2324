class Carrito:
    '''
    1. Gestionar carrito de compra
    2.1. Anyadir productos al carrito
    2.2. Eliminar productos del carrito
    2.3. Eliminar linea de compra
    2.4. Calcular importe
    '''
    def __init__(self):
        self.carrito: dict = dict()
    
    def add_product(self, product: str, qty: int) -> None:
        if product in self.carrito.keys():
            self.carrito[product] += qty
        else:
            self.carrito[product] = qty

    def decrement_product(self, product: str) -> None:
        if product in self.carrito.keys():
            self.carrito[product] -= 1
            if self.carrit[product] <= 0:
                self.delete_line(product)
    
    def delete_line(self, product: str) -> None:
        if product in self.carrito.keys():
            self.carrito.delete(product)
    
    def calculate_total(self) -> int:
        total: int = 0
        for qty in self.carrito.values():
            total += qty
            
        return total
        
    def show_lines(self) -> None:
        line_number: int = 1
        
        for product, qty in self.carrito.items():
            print(f"#{line_number}: {product} ... {qty}")
            line_number += 1
            
        def pay(self) -> None:
            print("Carrito pagat!")
            self.carrito.clear()
