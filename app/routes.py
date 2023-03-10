from app import app
from flask import jsonify, request
from app.controller.unit import Unit
from app.controller.wp import WP
from app.controller.jsa import JSA
from app.controller.user import User
from app.controller.presensi import Presensi
from app.controller.lingkungan import Lingkungan
from app.controller.guestbook import Guestbook

@app.route('/login', methods=['GET','POST'])
def login():
    object_user = User()
    if request.method == 'POST':
        result = object_user.login()

    return jsonify(result), 200

@app.route('/unit/<id>')
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


@app.route('/presensi', methods=['GET','POST'])
def presensi():
    if request.method == 'POST':
        object_presensi = Presensi()
        object_presensi.upload_presensi()

    response = {
        'message':'Data berhasil dikirim'
    }

    return jsonify(response), 200


@app.route('/presensi/<tanggal>')
def presensi_tanggal(tanggal):
    object_presensi = Presensi()
    result = object_presensi.get_presensi(tanggal)

    response = {
            "message":"Sukses",
            "data": result
        }
    
    return jsonify(response), 200


@app.route('/lingkungan/<lb3>', methods=['GET','POST'])
def limbah_b3(lb3):
    object_lingkungan = Lingkungan()

    if request.method == 'GET':
        if lb3 == 'all':
            result = object_lingkungan.get_lb3_all()
            response = {
            "message":"Sukses",
            "data": result
            }
        else:
            result = object_lingkungan.get_lb3(lb3)
            response = {
            "message":"Sukses",
            "data": result
            }

    if request.method == 'POST':
        object_lingkungan.upload_lb3()
        response = {
        'message':'Data berhasil dikirim'
        }

    return jsonify(response), 200


@app.route('/lingkungan/limbah/<path>', methods=['GET','POST'])
def limbah(path):
    object_lingkungan = Lingkungan()

    if request.method == 'GET':
        result = object_lingkungan.get_limbah(path)
        response = {
            "message":"Sukses",
            "data": result
        }
    
    if request.method == 'POST':
        object_lingkungan.upload_limbah()
        response = {
            'message':'Data berhasil dikirim'
        }

    return jsonify(response), 200


@app.route('/lingkungan/limbah/debit')
def debit_limbah():
    object_lingkungan = Lingkungan()
    result = object_lingkungan.get_debit_limbah()
    response = {
            "message":"Sukses",
            "data": result
        }
    
    return jsonify(response), 200


@app.route('/guestbook', methods=['GET','POST'])
def guestbook():
    object_guest = Guestbook()
    if request.method == 'POST':
        result = object_guest.upload_guest()
        
        response = {
            'message':'Data berhasil dikirim',
            'data': result
        }

    return jsonify(response), 200


@app.route('/test')
def test():
    object_presensi = Presensi()
    result = object_presensi.validation('ARVI BRAYEN WOWILING', '2023-02-08 21:13:47')

    print(len(result))

    response = {
            "message":"Sukses",
            "data": result
        }
    
    return jsonify(response), 200


