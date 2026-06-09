with open ("Productos.txt","r") as archivo:
    for linea in archivo:
        linea=linea.strip()
        nombre, precio,cantidad= linea.split(",")
        print(f"Producto: {nombre.strip()} | Precio: ${precio.strip()} | Cantidad: {cantidad.strip()}")

nombre=input("Ingrese un nombre: ")
precio=input("Ingrese el precio: ")
cantidad=input("Ingrese la cantidad: ")

with open("Productos.txt","a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")
print("Producto agregado correctamente.")

productos=[]
with open("Productos.txt","r") as archivo:
    for linea in archivo:
        nombre,precio,cantidad=linea.strip().split(",")

        producto={
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio
            }
        productos.append(producto)

nombre_buscado=input("Ingrese el nombre del producto: ")
encontrado= False

for producto in productos:
    if producto["nombre"].lower() == nombre_buscado.lower():
        print("\nProducto encontrado:")
        print(f"Nombre: {producto['nombre']} - ${producto['precio']} - Unidades: {producto['cantidad']}")
        encontrado=True
        break
if not encontrado:
    print("Error, el producto no existe")

with open("Productos.txt", "w") as archivo:
    for producto in productos:
        archivo.write(
            f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n"
        )

