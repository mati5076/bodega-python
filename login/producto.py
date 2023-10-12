class Producto:
    def __init__(self,codigo_de_barra,nombre_producto,categoria , marca , precio_unitario , cantidad_total_almacen , stock):
        self.codigo_de_barra = codigo_de_barra
        self.nombre_producto = nombre_producto
        self.categoria = categoria
        self.marca = marca
        self.precio_unitario = precio_unitario
        self.cantidad_total_almacen = cantidad_total_almacen
        self.stock = stock

    def contador_bodega(self):
        i = 0
        self.stock = []
        productos = int(input("ingresa cuantos productos quieres poner"))
        while i < productos:
            cuanto_tienes = input("ingresa los productos: ")
            self.stock.append(cuanto_tienes)
            cantidad_stock = len(self.stock)
            i+=1
        print(cantidad_stock)

    def calcular_precios(self):
        precio = int(input("ingrese la cantidad de precios :"))
        self.precio_unitario =[]
        a = 0
        while a < precio:
            precios = int(input(f"los precios son {a}"))
            self.precio_unitario.append(precios)
            a+=1
        print(self.precio_unitario)
