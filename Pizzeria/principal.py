import stock, cocina, pagos

def interificie_usuario():
    print("Bienvenido a Pizzeria MVM")
    pizza = input("Introduce el nombre de tu pizza: ")
    ingredientes = input("Introduce los ingredientes que quieres (separados por comas): ").split(",")
    return {"pizza": pizza, "ingredientes": ingredientes}

pedido_actual = interificie_usuario()

if stock.verificar_stock(stock, pedido_actual):
    cocina.cocina(pedido_actual)
    cocina.control_calidad()
    stock = stock.actualizar_stock(stock, pedido_actual)
    coste = pagos.calculo_costes(pedido_actual)
    pagos.imprimir_factura(pedido_actual, coste)
else:
    print("No tenemos alguno de los ingredientes")