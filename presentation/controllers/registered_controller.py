import sys
from pathlib import Path

file = Path(__file__).resolve()
package_root = file.parents[2]
sys.path.append(str(package_root))

from flask import jsonify
from flask import request
from flask import abort
from flask import Blueprint
from flask_cors import cross_origin

from infrastructure.repository.registered_repository import Registered_repository

registered_blueprint = Blueprint('registered_blueprint', __name__)
registered = Registered_repository()

@registered_blueprint.route('/registered', methods=['POST'])
@cross_origin()
def create_registered():
    if not request.json:
        abort(400)
    registered = Registered_repository(request.json['id'], request.json['name'], request.json['email'], request.json['password'])
    registered.insert()
    return jsonify(registered)

@registered_blueprint.route('/registered', methods=['GET'])
@cross_origin()
def get_registereds():
    registereds = registered.get_all()
    return jsonify(registereds)

@registered_blueprint.route('/registered/<int:id>', methods=['GET'])
@cross_origin()
def get_registered(id):
    registered = registered.get(id)
    return jsonify(registered)

@registered_blueprint.route('/registered/<int:id>', methods=['DELETE'])
@cross_origin()
def delete_registered(id):
    registered = registered.delete(id)
    return jsonify(registered)
