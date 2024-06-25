from flask import Blueprint,request,render_template
from models import Sucursal,Paquete
salida=Blueprint("salidatransporte",__name__)

@salida.route("/Transporte",methods=["GET", "POST"])
def transporte():
    if request.method == "GET":
        id=request.form.get("sucursal")
        sucursales=Sucursal.query.all()
        return render_template("transporte.html",sucursales=sucursales,sucursal_id=id)
    else:
        idmisucursal=request.form.get("sucursal_id")
        idsucursal = request.form.get("sucursal")
        #,idsucursal=idmisucursal
        listapaquetes=Paquete.query.filter_by(entregado=0,idrepartidor = 0).all()
        return render_template("paquetes.html",paquetes=listapaquetes,idsucursal=idsucursal)