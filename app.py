from flask import Flask, render_template, request
from entities.pedido_total import Pedido_total
from entities.producto import Producto
from entities.subtotal_producto import ProductoPedido
from enums.tipo_producto import TipoProducto
from data.menu import menu

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', menu=menu)

if __name__ == '__main__':
    app.run()