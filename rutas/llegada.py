from flask import Blueprint, request, render_template, flash, redirect, url_for
from models import Transporte, db
from datetime import datetime

llegada = Blueprint("llegada", __name__)

@llegada.route("/llegada", methods=['GET', 'POST'])
def llegadapaquete():
    if request.method == 'GET':
        id = request.args.get("sucursal")
        listatransportes = Transporte.query.filter_by(idsucursal=id, fechahorallegada=None).all()
        return render_template("llegada.html", id=id, lista=listatransportes)
    else:
        id = request.form.get("misucursal")
        transportes = request.form.getlist("transportes")
        for transporte_id in transportes:
            T = Transporte.query.filter_by(id=transporte_id).first()
            if T:
                T.fechahorallegada = datetime.now()
                db.session.commit()
        flash('Registro llegada', 'success')
        return redirect(url_for('despachante.bienvenido',sucursal=id))
