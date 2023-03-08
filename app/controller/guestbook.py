import os
from app import app
from db import connection
from flask import request
from app import utils
from datetime import datetime

class Guestbook:
    def upload_guest(self):
        nama_lengkap = request.form['nama_lengkap']
        instansi = request.form['instansi']
        hp = request.form['hp']
        tujuan = request.form['tujuan']
        foto = request.form['foto']

        nama_foto = self.upload_photo(foto, nama_lengkap)
        self.insert_guest(nama_lengkap, instansi, hp, tujuan, nama_foto)

        return nama_lengkap


    def insert_guest(self, nama_lengkap, instansi, hp, tujuan, foto):
        query = f"INSERT INTO guestbook (nama_lengkap, instansi, hp, tujuan, foto) VALUES ('{nama_lengkap}','{instansi}','{hp}','{tujuan}','{foto}')"
        connection(query, 'insert')


    def upload_photo(self, foto, nama):
        photo = utils.base64topng(foto)
        tanggal = datetime.today().strftime('%Y%m%d%H%M%S')
        renamefile = f"{tanggal}-{nama.replace(' ', '')}.png"
        photo.save(os.path.join(app.config['FOTO_TAMU'], renamefile))
        return renamefile
