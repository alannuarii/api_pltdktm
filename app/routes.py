import os
from app import app
from flask import jsonify, request
from app.controller.unit import Unit
from app.controller.wp import WP
from app.controller.jsa import JSA

@app.route('/<id>')
def get_data(id):
    object = Unit()
    result = object.get_all_by_id(id)

    return jsonify(result), 200


@app.route('/working-permit', methods=['GET','POST'])
def working_permit():
    if request.method == 'POST':
        # print(request.form)
        # print(request.files['hirarc'].filename)
        object_wp = WP()
        object_wp.upload_wp()

    response = {
        "message":"Data berhasil dikirim"
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