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

from infrastructure.repository.event_repository import Event_repository

event_blueprint = Blueprint('event_blueprint', __name__)
event = Event_repository()

@event_blueprint.route('/event', methods=['POST'])
@cross_origin()
def create_event():
    if not request.json:
        abort(400)
    event = Event_repository(request.json['id'], request.json['title'], request.json['theme'], request.json['description'], request.json['date_time'], request.json['platform'], request.json['access_link'], request.json['id_administrator'])
    event = event.insert()
    return jsonify(event)

@event_blueprint.route('/event', methods=['GET'])
@cross_origin()
def get_events():
    events = event.getAll()
    return jsonify(events)

@event_blueprint.route('/event/<int:id>', methods=['GET'])
@cross_origin()
def get_event(id):
    event = event.get(id)
    return jsonify(event)

@event_blueprint.route('/event/<int:id>', methods=['DELETE'])
@cross_origin()
def delete_event(id):
    event = event.delete(id)
    return jsonify(event)
