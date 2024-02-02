stock = {
    'queso': 10,
    'tomate': 0,
    'pinya': 1
}

def verificar_stock(stock, pedido):
    for ingrediente in pedido['ingredientes']:
        if ingrediente not in stock or stock[ingrediente] == 0:
            return False
    return True

def actualizar_stock(stock, pedido):
    for ingrediente in pedido['ingredientes']:
        stock[ingrediente] -= 1
        if stock[ingrediente] == 0:
            stock = abastecer(stock, ingrediente, 10)
    return stock

def abastecer(stock, ingrediente, cantidad):
    stock[ingrediente] = cantidad
    return stock