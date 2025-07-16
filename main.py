inventario = {}

cantidad = int(input("\n¿Cuántos productos desea ingresar?: "))

for i in range(cantidad):
    print(f"\n Producto #{i + 1}")

    while True:
        codigo = int(input("Ingrese el código numérico del producto: "))
        try:
            int_codigo = int(codigo)
            if codigo in inventario:
                print("EsTe código ya existe. Ingrese uno diferente.")
            else:
                break
        except ValueError:
            print("El código debe contener solo números.")