# Dependencias de la aplicación
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creacion del nombre y la conexion a la base de datos
database_name = 'EventComp'
database_path = 'postgres://{}/{}'.format('localhost:8085', database_name)
database = SQLAlchemy()

# Creacion de la funcion para crear la aplicacion
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path   # Conexion a la base de datos
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False    # Desactivar el rastreo de modificaciones
    database.app = app                                      # Asignar la aplicacion a la base de datos
    database.init_app(app)                                  # Inicializar la base de datos
    database.create_all()                                   # Crear la base de datos
