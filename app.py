from flask import Flask, render_template, request
from entities.pedidoTotal import PedidoTotal
from entities.producto import Producto
from entities.subtotalProducto import ProductoPedido
from enums.tipoProducto import TipoProducto

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()