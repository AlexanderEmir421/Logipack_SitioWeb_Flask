from flask import Blueprint,request,render_template
from models import Sucursal

registrar=Blueprint("menuregistrarpaquete",__name__)

@registrar.route("/registropaq",methods=["POST"])
def registro():
    if request.method == "POST":
        idsucursal=request.form.get("sucursal")
        sucursalE = Sucursal.query.filter_by(id=idsucursal).first()        
        return render_template("registrarpaquete.html",sucursal=sucursalE)
    