# Se importa Flask
from flask import Flask

import sys
from pathlib import Path

# Se importa el archivo de configuracion para el path
file = Path(__file__).resolve()
package_root = file.parents[1]
sys.path.append(str(package_root))

# se importa la conexion a la base de datos y los controladores de admin, event, participant, registered, speaker
from infrastructure.repository.db_connection import setup_db
from controllers.admin_controller import admin_blueprint
from controllers.event_controller import event_blueprint
from controllers.participant_controller import participant_blueprint
from controllers.registered_controller import registered_blueprint
from controllers.speaker_controller import speaker_blueprint

# Funcion principal para iniciar la aplicacion
def create_app():
    # Se crea la aplicacion Flask
    app = Flask(__name__)
    # Se registran los blueprints de la aplicacion (PARTE DEL PRINCIPIO SOLID OPEN CLOSED)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(event_blueprint)
    app.register_blueprint(participant_blueprint)
    app.register_blueprint(registered_blueprint)
    app.register_blueprint(speaker_blueprint)
    setup_db(app)
    return app
