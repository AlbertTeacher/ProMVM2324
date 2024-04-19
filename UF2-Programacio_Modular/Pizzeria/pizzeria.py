stock = {
    'queso': 10,
    'tomate': 0,
    'pinya': 1
}

def interificie_usuario():
    print("Bienvenido a Pizzeria MVM")
    pizza = input("Introduce el nombre de tu pizza: ")
    ingredientes = input("Introduce los ingredientes que quieres (separados por comas): ").split(",")
    return {"pizza": pizza, "ingredientes": ingredientes}

def verificar_stock(stock, pedido):
    for ingrediente in pedido['ingredientes']:
        if ingrediente not in stock or stock[ingrediente] == 0:
            return False
    return True

def cocina(pedido):
    print(f"Cocinando la pizza {pedido['pizza']} con los ingredientes {', '.join(pedido['ingredientes'])}")

def control_calidad():
    print("Esta todo perfecto")

def actualizar_stock(stock, pedido):
    for ingrediente in pedido['ingredientes']:
        stock[ingrediente] -= 1
        if stock[ingrediente] == 0:
            stock = abastecer(stock, ingrediente, 10)
    return stock

def abastecer(stock, ingrediente, cantidad):
    stock[ingrediente] = cantidad
    return stock

def calculo_costes(pedido):
    return len(pedido['ingredientes'])

def imprimir_factura(pedido, coste):
    print(f"Factura - Pizza {pedido['pizza']}, Coste {coste} euros")

pedido_actual = interificie_usuario()

if verificar_stock(stock, pedido_actual):
    cocina(pedido_actual)
    control_calidad()
    stock = actualizar_stock(stock, pedido_actual)
    coste = calculo_costes(pedido_actual)
    imprimir_factura(pedido_actual, coste)
else:
    print("No tenemos alguno de los ingredientes")