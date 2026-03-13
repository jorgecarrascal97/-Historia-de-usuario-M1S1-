# -Historia-de-usuario-M1S1-
      Registrar productos con su nombre, precio y cantidad en un programa simple.     Calcular operaciones básicas como total de unidades y costo aproximado.     Aplicar fundamentos de programación: entrada de datos, variables, operaciones matemáticas y salidas en consola.

      


nombre = input("Ingrese el nombre del producto: ")
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio < 0:
            print("Error: El precio no puede ser negativo.")
        else:
            break
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio.")
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if cantidad < 0:
            print("Error: La cantidad no puede ser negativa.")
        else:
            break
    except ValueError:
        print("Error: Debe ingresar un número entero válido para la cantidad.")

costo_total = precio * cantidad

print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")
