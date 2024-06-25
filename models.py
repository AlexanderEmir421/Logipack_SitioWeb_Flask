from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sucursal(db.Model):
    __tablename__ = 'sucursal'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    provincia = db.Column(db.String(100), nullable=False)
    localidad = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    repartidores = db.relationship('Repartidor', backref='sucursal', lazy=True)
    paquetes = db.relationship('Paquete', backref='sucursal', lazy=True)
    transportes = db.relationship('Transporte', backref='sucursal', lazy=True)


class Transporte(db.Model):
    __tablename__ = 'transporte'
    id = db.Column(db.Integer, primary_key=True)
    numerotransporte = db.Column(db.Integer, nullable=False)
    fechahorasalida = db.Column(db.DateTime, nullable=False)
    fechahorallegada = db.Column(db.DateTime, nullable=True)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    paquetes = db.relationship('Paquete', backref='transporte', lazy=True)



class Repartidor(db.Model):
    __tablename__ = 'repartidor'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer,nullable = False)
    nombre = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(20), nullable=False)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    paquetes = db.relationship('Paquete', backref='repartidor', lazy=True)


class Paquete(db.Model):
    __tablename__ = 'paquete'
    id = db.Column(db.Integer, primary_key=True)
    numeroenvio = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    nomdestinatario = db.Column(db.String(100), nullable=False)
    dirdestinatario = db.Column(db.String(200), nullable=False)
    entregado = db.Column(db.Boolean, default=False)
    observaciones = db.Column(db.String(200))
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    idtransporte = db.Column(db.Integer, db.ForeignKey('transporte.id'), nullable=True)
    idrepartidor = db.Column(db.Integer, db.ForeignKey('repartidor.id'), nullable=True)
