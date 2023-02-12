from app import app
from db import connection
from flask import request

class Lingkungan:
    def upload_lb3(self):
        tanggal = request.form['tanggal']
        jenis = request.form['jenis']
        status = request.form['status']
        jumlah = request.form['jumlah']

        self.insert_lb3(tanggal, jenis, status, jumlah)

    def insert_lb3(self, tanggal, jenis, status, jumlah):
        query = f"INSERT INTO lb3 (tanggal, jenis, status, jumlah) VALUES ('{tanggal}', '{jenis}', '{status}', {jumlah})"
        connection(query, 'insert')