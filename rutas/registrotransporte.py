from flask import Blueprint, request, render_template, flash, redirect, url_for
from models import db,Paquete,Transporte,Sucursal
from datetime import datetime
import random
import logging

registrotransporte=Blueprint("registrotransporte",__name__)

@registrotransporte.route("/registrotransporte",methods=["POST"])
def registrartransportep():
    if request.method == "POST":
        try:
            misucursal=request.form.get("misucursal")
            sucursal=request.form.get("sucursal_id")
            paquetes=request.form.getlist("paquetes")
            creatransporte=Transporte(numerotransporte=random.randint(1000, 9999)
            ,fechahorasalida=datetime.now()
            ,fechahorallegada=None
            ,idsucursal=sucursal)
            db.session.add(creatransporte)
            db.session.commit()                         
            for p in paquetes:
                paquete=Paquete.query.filter_by(id=p).first()
                if paquete:
                    paquete.idtransporte=creatransporte.id
                    db.session.commit()
            flash('Paquetes asignados a transportes con exito', 'success')           
            return redirect(url_for('despachante.bienvenido', sucursal=misucursal))
        except Exception as e:
            logging.warning(e)
            flash(f'Error al asignar transporte: {e}', 'danger')
            m=Sucursal.query.filter_by(id=misucursal).first() 
            return render_template("paquetes.html",idsucursal=sucursal,misucursal=m.numero)        
