from flask import Blueprint, request, render_template, flash, redirect, url_for
from models import db, Paquete, Sucursal
import random
import logging

registrarpaquete = Blueprint("registrarpaquete", __name__)

@registrarpaquete.route("/registropaquete", methods=["POST"])
def registro():
    if request.method == "POST":
        id = request.form.get("sucursal_id")
        peso = request.form.get("peso")
        nombre = request.form.get("nombre")
        direccion = request.form.get("direccion")
        numE = random.randint(1000, 9999)
        try:
            peso = float(peso)
            nuevo_paquete = Paquete(
                numeroenvio=numE, peso=peso, nomdestinatario=nombre,
                dirdestinatario=direccion, idsucursal=id, idrepartidor=0,
                entregado=0
            )
            db.session.add(nuevo_paquete)
            db.session.commit()
            flash('Paquete registrado exitosamente', 'success')
            return redirect(url_for('despachante.bienvenido', sucursal=id))
        except ValueError:
            flash('El peso debe ser un número.', 'danger')
        except Exception as e:
            logging.warning(e)
            flash(f'Error al registrar el paquete: {e}', 'danger')
        
        # Renderiza la plantilla nuevamente con los datos de la sucursal si hay un error
        sucursal = Sucursal.query.filter_by(id=id).first()
        return render_template("registrarpaquete.html", sucursal=sucursal)
