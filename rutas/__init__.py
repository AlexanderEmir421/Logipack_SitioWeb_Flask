from .acceso import acceso
from .sucursales import sucursales_bp
from .menuregistrarpaquete import registrar
from .registrarpaquete import registrarpaquete
from .despachante import despachante
from .salidatransporte import salida
from .registrotransporte import registrotransporte
from .llegada import llegada
def rutas(app):
    app.register_blueprint(acceso)
    app.register_blueprint(sucursales_bp)
    app.register_blueprint(registrar)
    app.register_blueprint(registrarpaquete)
    app.register_blueprint(despachante)
    app.register_blueprint(salida)
    app.register_blueprint(registrotransporte)
    app.register_blueprint(llegada)