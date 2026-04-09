productos = [
    {"id": 1, "nombre": "Camiseta", "precio": 25000},
    {"id": 2, "nombre": "Pantalón Jeans", "precio": 55000},
    {"id": 3, "nombre": "Zapatos deportivos", "precio": 95000}
]

def ver_productos():
    print("\nProductos disponibles:")
    for p in productos:
        print(str(p["id"]) + ". " + p["nombre"] + " - $" + str(p["precio"]))
    print("")

def buscar_producto(id_buscar):
    for p in productos:
        if p["id"] == id_buscar:
            return p
    return None