from flask import Blueprint,render_template,request

acceso = Blueprint("acceso", __name__)

@acceso.route("/acceso")
@acceso.route("/")
def acceder():
    return render_template('acceso.html')


