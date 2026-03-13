# Programa: inventario.py
# Este programa solicita al usuario el nombre de un producto, su precio y la cantidad.
# Valida que precio y cantidad sean valores numéricos correctos antes de continuar.

# -------------------------------
# Solicitar nombre del producto
# -------------------------------
nombre = input("Ingrese el nombre del producto: ")

# -------------------------------
# Solicitar y validar el precio
# Se repite hasta que el usuario ingrese un número válido
# -------------------------------
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio < 0:
            print("Error: El precio no puede ser negativo.")
        else:
            break
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio.")

# -------------------------------
# Solicitar y validar la cantidad
# Se repite hasta que el usuario ingrese un número entero válido
# -------------------------------
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if cantidad < 0:
            print("Error: La cantidad no puede ser negativa.")
        else:
            break
    except ValueError:
        print("Error: Debe ingresar un número entero válido para la cantidad.")

# -------------------------------
# Cálculo del costo total
# Multiplica el precio por la cantidad
# -------------------------------
costo_total = precio * cantidad

# -------------------------------
# Mostrar resultados en consola
# Se presenta la información de forma clara
# -------------------------------
print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")

# -----------------------------------------------------------
# Comentario general del programa
# Este programa solicita al usuario el nombre de un producto,
# su precio y la cantidad. Luego valida que el precio sea un
# número decimal y que la cantidad sea un número entero. Si el
# usuario ingresa un dato inválido, el sistema muestra un error
# y solicita nuevamente el dato. Finalmente, calcula el costo
# total multiplicando el precio por la cantidad y muestra los
# resultados en la consola.
# -----------------------------------------------------------
