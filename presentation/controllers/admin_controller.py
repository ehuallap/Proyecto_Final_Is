import sys
from pathlib import Path

# Para poder importar el archivo de configuracion de la base de datos
file = Path(__file__).resolve()
package_root = file.parents[2]
sys.path.append(str(package_root))

# Dependencias de Flask y flask_cors
from flask import jsonify
from flask import request
from flask import abort
from flask import Blueprint
from flask_cors import cross_origin

# Se importa la clase del repositorio de Administrador
from infrastructure.repository.admin_repository import Administrator_repository

# Se registra el blueprint del Administrador, principio SOLID de OPEN CLOSED
admin_blueprint = Blueprint('admin_blueprint', __name__)
admin = Administrator_repository()

# Se crea la ruta para crear un Administrador, el metodo POST
@admin_blueprint.route('/admin', methods=['POST'])
@cross_origin()
def create_admin():
    # Se verifica que el request sea un JSON, si no es asi, se aborta con un 400 (PROGRAMACION DEFENSIVA)
    if not request.json:
        abort(400)
    # Se crea un objeto de la clase Administrador, con los datos del request
    admin = Administrator_repository(request.json['id'], request.json['name'], request.json['email'], request.json['password'])
    # Se inserta el objeto en la base de datos
    admin = admin.insert()
    # Se retorna el objeto creado
    return jsonify(admin)

# Se crea la ruta para obtener todos los Administradores, el metodo GET
@admin_blueprint.route('/admin', methods=['GET'])
@cross_origin()
def get_admins():
    # Se obtienen todos los Administradores de la base de datos
    admins = admin.get_all()
    # Se retornan los Administradores
    return jsonify(admins)

# Se crea la ruta para obtener un Administrador, el metodo GET
@admin_blueprint.route('/admin/<int:id>', methods=['GET'])
@cross_origin()
def get_admin(id):
    admin = admin.get(id)
    return jsonify(admin)

# Se crea la ruta para eliminar un Administrador, el metodo DELETE
@admin_blueprint.route('/admin/<int:id>', methods=['DELETE'])
@cross_origin()
def delete_admin(id):
    admin = admin.delete(id)
    return jsonify(admin)
