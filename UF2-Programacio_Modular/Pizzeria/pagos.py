def calculo_costes(pedido):
    return len(pedido['ingredientes'])

def imprimir_factura(pedido, coste):
    print(f"Factura - Pizza {pedido['pizza']}, Coste {coste} euros")