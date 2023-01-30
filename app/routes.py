from app import app
from flask import jsonify, request
from app.controller.unit import Unit
from app.controller.wp import WP
from app.controller.jsa import JSA
from app.controller.user import User

@app.route('/login', methods=['GET','POST'])
def login():
    object_user = User()
    if request.method == 'POST':
        result = object_user.login()

    return jsonify(result), 200

@app.route('/<id>')
def get_data(id):
    object_unit = Unit()
    result = object_unit.get_all_by_id(id)

    return jsonify(result), 200


@app.route('/working-permit', methods=['GET','POST'])
def working_permit():
    object_wp = WP()

    if request.method == 'GET':
        result = object_wp.get_wp()
        response = {
            "message":"Sukses",
            "data": result
        }

    if request.method == 'POST':
        object_wp.upload_wp()
        response = {
            "message": "Data berhasil dikirim"
        }

    return jsonify(response), 200


@app.route('/working-permit/<id>')
def wp_id(id):
    object_wp = WP()
    result = object_wp.get_wp_id(id)
    response = {
        "message":"Sukses",
        "data": result
    }

    return jsonify(response), 200


@app.route('/jsa', methods=['GET','POST'])
def jsa():
    if request.method == 'POST':
        # print(request.form.getlist('tahap_pekerjaan'))
        object_jsa = JSA()
        object_jsa.upload_jsa()

    response = {
        'message':'Data berhasil dikirim'
    }

    return jsonify(response), 200

@app.route('/jsa/<id>')
def jsa_id(id):
    object_jsa = JSA()
    result = object_jsa.get_jsa_id(id)
    response = {
        "message":"Sukses",
        "data": result
    }

    return jsonify(response), 200


@app.route('/test')
def test():
    object_user = User()
    result = object_user.set_password('123456')

    return jsonify(result), 200
