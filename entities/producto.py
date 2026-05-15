from enums.tipo_producto import TipoProducto

class Producto:
    def __init__(self, idProducto: int, nombre: str, precio: float, tipo: TipoProducto):
        self.idProducto = idProducto
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo

    def __str__(self):
        return f"Producto(ID: {self.idProducto}, Nombre: {self.nombre}, Precio: {self.precio}, Tipo: {self.tipo.name})"