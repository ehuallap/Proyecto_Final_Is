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

from infrastructure.repository.participant_repository import Participant_repository

participant_blueprint = Blueprint('participant_blueprint', __name__)
participant = Participant_repository()

@participant_blueprint.route('/participant', methods=['POST'])
@cross_origin()
def create_participant():
    if not request.json:
        abort(400)
    participant = Participant_repository(request.json['id'], request.json['name'], request.json['email'], request.json['password'], request.json['universidad'], request.json['ciclo'])
    participant.insert()
    return jsonify(participant)

@participant_blueprint.route('/participant', methods=['GET'])
@cross_origin()
def get_participants():
    participants = participant.get_all()
    return jsonify(participants)

@participant_blueprint.route('/participant/<int:id>', methods=['GET'])
@cross_origin()
def get_participant(id):
    participant = participant.get(id)
    return jsonify(participant)

@participant_blueprint.route('/participant/<int:id>', methods=['DELETE'])
@cross_origin()
def delete_participant(id):
    participant = participant.delete(id)
    return jsonify(participant)
