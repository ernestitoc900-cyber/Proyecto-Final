from enums.tipo_producto import TipoProducto
from entities.producto import Producto

menu = [
    Producto(1, "Coca-Cola", 25, TipoProducto.BEBIDA),
    Producto(2, "Café", 40, TipoProducto.BEBIDA),
    Producto(3, "Torta", 49.50, TipoProducto.COMIDA),
    Producto(4, "Pay", 60, TipoProducto.POSTRE),
    Producto(5, "Galleta", 30, TipoProducto.OTRO)
]