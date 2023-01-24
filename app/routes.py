import os
from app import app
from flask import jsonify, request
from app.controller.unit import Unit

@app.route('/<id>')
def get_data(id):
    object = Unit()
    result = object.get_all_by_id(id)

    return jsonify(result), 200


@app.route('/working-permit', methods=['GET','POST'])
def working_permit():
    if request.method == 'POST':
        # hirarc = request.files['hirarc']

        # hirarc.save(os.path.join(app.config['FILE_HIRARC'], hirarc.filename))
        print(request.form)
    # print(request.files)
    response = {
        "message":"Data berhasil dikirim"
    }

    return jsonify(response), 200

@app.route('/jsa', methods=['GET','POST'])
def jsa():
    if request.method == 'POST':
        print(request.form)

    response = {
        'message':'Data berhasil dikirim'
    }

    return jsonify(response), 200