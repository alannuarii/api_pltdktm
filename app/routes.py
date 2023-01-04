from app import app
from flask import jsonify, request
from app.controller.unit import Unit

@app.route('/<id>')
def get_data(id):
    object = Unit()
    result = object.get_all_by_id(id)

    return jsonify(result), 200

