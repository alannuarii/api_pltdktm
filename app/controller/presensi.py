import os
from app import app
from flask import request
from app import utils
from datetime import datetime
from db import connection


class Presensi:
    def upload_presensi(self):
        nama = request.form['nama']
        waktu = request.form['waktu']
        foto = request.form['foto']
        nama_foto = self.upload_photo(foto, waktu, nama)
        self.insert_presensi(nama, waktu, nama_foto)

    def insert_presensi(self, nama, waktu, foto):
        query = f"INSERT INTO presensi (nama, waktu, foto) VALUES ('{nama}', '{waktu}', '{foto}')"
        connection(query, 'insert')

    def upload_photo(self, pic, waktu, nama):
        photo = utils.base64topng(pic)
        str_datetime = datetime.strptime(waktu, '%Y-%m-%d %H:%M:%S').strftime('%Y%m%d%H%M%S')
        renamefile = f"{str_datetime}-{nama}.png"
        photo.save(os.path.join(app.config['FOTO_PRESENSI'], renamefile))
        return renamefile

    def get_presensi(self, tanggal):
        query = f"SELECT * FROM presensi WHERE DATE(waktu) = '{tanggal}' ORDER BY waktu"
        result = connection(query, 'select')
        return result
        