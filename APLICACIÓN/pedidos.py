def agregar_producto(pedido_actual, producto, cantidad):
    subtotal = producto["precio"] * cantidad
    pedido_actual.append({
        "nombre": producto["nombre"],
        "cantidad": cantidad,
        "valor_unitario": producto["precio"],
        "subtotal": subtotal
    })
    return pedido_actual