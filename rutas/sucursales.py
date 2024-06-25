from flask import Blueprint,render_template,request
from models import Sucursal

sucursales_bp = Blueprint("sucursales", __name__)

@sucursales_bp.route("/sucursales")
def sucursales():
    listasucursal=Sucursal.query.order_by(Sucursal.numero).all()    
    return render_template('sucursales.html',lista=listasucursal)
    