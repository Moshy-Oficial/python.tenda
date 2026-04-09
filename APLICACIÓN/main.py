import productos as prod
import pedidos as ped
import datetime

mi_pedido = []

while True:
    print("\n=== TIENDA EN LÍNEA ===")
    print("1. Ver productos")
    print("2. Agregar al pedido")
    print("3. Ver mi pedido actual")
    print("4. Finalizar compra")
    print("5. Ver historial de compras")
    print("6. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        prod.ver_productos()
    
    elif opcion == "2":
        prod.ver_productos()
        try:
            id_prod = int(input("Ingresa el ID del producto: "))
            cant = int(input("Cantidad: "))
            producto_encontrado = prod.buscar_producto(id_prod)
            if producto_encontrado:
                mi_pedido = ped.agregar_producto(mi_pedido, producto_encontrado, cant)
                print("Producto agregado correctamente!")
            else:
                print("No encontré ese producto")
        except:
            print("Por favor ingresa números válidos")
    
    elif opcion == "3":
        if len(mi_pedido) == 0:
            print("Todavía no tienes productos en el pedido")
        else:
            print("\nTu pedido actual:")
            for item in mi_pedido:
                print(str(item["cantidad"]) + " x " + item["nombre"] + " = $" + str(item["subtotal"]))
            total = sum(item["subtotal"] for item in mi_pedido)
            print("Total hasta ahora: $" + str(total))
    
    elif opcion == "4":
        if len(mi_pedido) == 0:
            print("No tienes nada para comprar")
        else:
            fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            with open("historial.txt", "a") as f:
                f.write("\nCompra realizada el " + fecha + "\n")
                for item in mi_pedido:
                    f.write(str(item["cantidad"]) + " " + item["nombre"] + " $" + str(item["valor_unitario"]) + " c/u  subtotal $" + str(item["subtotal"]) + "\n")
                total_final = sum(item["subtotal"] for item in mi_pedido)
                f.write("TOTAL: $" + str(total_final) + "\n")
            print("¡Compra finalizada! Total: $" + str(total_final))
            mi_pedido = []
    
    elif opcion == "5":
        try:
            with open("historial.txt", "r") as f:
                print(f.read())
        except:
            print("Todavía no hay compras registradas")
    
    elif opcion == "6":
        print("Gracias por visitar la tienda. Hasta pronto!")
        break
    
    else:
        print("Opción no válida, intenta de nuevo")