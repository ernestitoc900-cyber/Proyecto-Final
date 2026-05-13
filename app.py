from flask import Flask, render_template, request
from entities.pedido_total import PedidoTotal
from entities.producto import Producto
from entities.subtotal_producto import ProductoPedido
from enums.tipo_producto import TipoProducto

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()