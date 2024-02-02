stock = {
    'queso': 10,
    'tomate': 0,
    'pinya': 1
}
def interficie_usuari():
    print("Bienvenido a Pizzeria MVM")
    pizza = input("Introduce el nombre de la pizza: ")
    ingredientes = input("Introduce los ingredientes (separados por comas): ").split(',')
    return {"pizza": pizza, "ingredientes": ingredientes}

def verificar_stock(stock, pedido):
    for ingrediente in pedido['ingredientes']:
        if ingrediente in stock and stock[ingrediente] != 0:
            return True
    return False

def cocina(pedido):
    print(f"Cocinado la pizza {pedido['pizza']} con los ingredientes {', '.join(pedido['ingredientes'])}")

def control_calidad():
    print("Todo esta correcto")

def reabastecer(stock, ingrediente, cantidad):
    stock[ingrediente] = cantidad

def actualizar_stock(stock, pedido):
    for ingrediente in pedido['ingredientes']:
        stock[ingrediente] -= 1
        if stock[ingrediente] == 0:
            reabastecer(stock, ingrediente, 10)
    return stock

def calculo_costes(pedido):
    return len(pedido['ingredientes'])

def facturacion(pedido, coste):
    print(f"Factura - Pizza {pedido['pizza']}, Coste {coste} euros")

pedido_actual = interficie_usuari()

if verificar_stock(stock, pedido_actual):
    cocina(pedido_actual)
    control_calidad()
    stock = actualizar_stock(stock, pedido_actual)
    coste = calculo_costes(pedido_actual)
    facturacion(pedido_actual, coste)
else:
    print("No tenemos alguno de los ingredientes")