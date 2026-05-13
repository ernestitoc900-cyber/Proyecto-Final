from enums.tipo_producto import Tipo_producto


class Producto:
    def __init__(self, idProducto: int, nombre: str, precio: float, tipo: Tipo_producto):
        self.idProducto = idProducto
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo