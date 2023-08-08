# Dependencias del proyecto
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

# Crear el objeto de aplicación
app = Flask(__name__)
#configurar app para conectarse a bd
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask-shopy-2687350'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Crear el objeto sqlalchemy
db = SQLAlchemy(app)
# Crear el objeto de migracion y activarlo
migrate = Migrate(app , db)

## Modelos <<entities>>
class Cliente(db.Model):
    
    __tablename__="clientes"
    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(128))
    email = db.Column(db.String(120))

class Producto(db.Model):
    __tablename__="productos"
    id = db.Column(db.Integer , primary_key=True)
    nombre = db.Column(db.String(64))
    precio = db.Column(db.Numeric(precision = 10 , scale = 2),nullable = False)
    imagen = db.Column(db.String(100))

class Ventas(db.Model):
    __tablename__="ventas"
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime, 
                      default = datetime.utcfromtimestamp)
    cliente_id = db.Column(db.Integer, 
                           db.ForeignKey('clientes.id'))
    

class Detalles(db.Model):
    __tablename__="detalles"
    id = db.Column(db.Integer, primary_key = True)
    venta_id = db.Column(db.Integer, 
                           db.ForeignKey('ventas.id'))
    producto_id = db.Column(db.Integer, 
                           db.ForeignKey('productos.id'))
    cantidad = db.Column(db.Integer)






