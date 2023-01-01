from app import app
from flask import jsonify, request
from app.controller.unit import Unit

@app.route('/')
def get_data():
    object = Unit()
    result = object.get_units()

    return jsonify(result), 200

