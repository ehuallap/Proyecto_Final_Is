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

from infrastructure.repository.speaker_repository import Speaker_repository

speaker_blueprint = Blueprint('speaker_blueprint', __name__)
speaker = Speaker_repository()

@speaker_blueprint.route('/speaker', methods=['POST'])
@cross_origin()
def create_speaker():
    if not request.json:
        abort(400)
    speaker = Speaker_repository(request.json['id'], request.json['name'], request.json['email'], request.json['password'])
    speaker.insert()
    return jsonify(speaker)

@speaker_blueprint.route('/speaker', methods=['GET'])
@cross_origin()
def get_speakers():
    speakers = speaker.get_all()
    return jsonify(speakers)

@speaker_blueprint.route('/speaker/<int:id>', methods=['GET'])
@cross_origin()
def get_speaker(id):
    speaker = speaker.get(id)
    return jsonify(speaker)

@speaker_blueprint.route('/speaker/<int:id>', methods=['DELETE'])
@cross_origin()
def delete_speaker(id):
    speaker = speaker.delete(id)
    return jsonify(speaker)
