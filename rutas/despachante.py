from flask import Blueprint,render_template,request,flash
from models import Sucursal

despachante=Blueprint("despachante",__name__)

@despachante.route("/Menudespachante", methods=["POST","GET"])
def bienvenido(): 
    if request.method == "POST":        
        idsucursal = request.form.get("sucursal")
    else:
        idsucursal = request.args.get("sucursal")  # Cambiado a args para GET
    
    return render_template("menudespachante.html", sucursal=idsucursal)