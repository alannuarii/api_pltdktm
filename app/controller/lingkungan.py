from db import connection
from flask import request
from datetime import datetime

class Lingkungan:

    #LB3
    def upload_lb3(self):
        tanggal = request.form['tanggal']
        jenis = request.form['jenis']
        status = request.form['status']
        jumlah = request.form['jumlah']

        self.insert_lb3(tanggal, jenis, status, jumlah)

    def insert_lb3(self, tanggal, jenis, status, jumlah):
        query = f"INSERT INTO lb3 (tanggal, jenis, status, jumlah) VALUES ('{tanggal}', '{jenis}', '{status}', {jumlah})"
        connection(query, 'insert')

    def get_lb3_all(self):
        query = f"SELECT * FROM lb3"
        result = connection(query, 'select')
        return result

    def get_lb3(self, lb3):
        query = f"SELECT * FROM lb3 WHERE jenis = '{lb3}' ORDER BY tanggal DESC"
        result = connection(query, 'select')
        return result
    

    # Air Limbah
    def upload_limbah(self):
        tanggal = request.form['tanggal']
        jenis = request.form['jenis']
        parameter = request.form['parameter']
        nilai = request.form['nilai']

        self.insert_limbah(tanggal, jenis, parameter, nilai)
        # for i in range(27):
        #     self.insert_limbah(f"2023-02-{i+1}", 'proses', 'debit', 0)

    def insert_limbah(self, tanggal, jenis, parameter, nilai):
        query = f"INSERT INTO limbah (tanggal, jenis, parameter, nilai) VALUES ('{tanggal}', '{jenis}', '{parameter}', {nilai})"
        connection(query, 'insert')

    def get_limbah(self, path):
        listPath = path.split('-')
        query = f"SELECT * FROM limbah WHERE YEAR(tanggal) = '{listPath[2]}' AND MONTH(tanggal) = '{listPath[3]}' AND jenis = '{listPath[0]}' AND parameter = '{listPath[1]}'"
        result = connection(query, 'select')
        return result
    
    def get_debit_limbah(self):
        now = datetime.now()
        month = now.strftime('%m')
        query = f"SELECT jenis, nilai FROM limbah WHERE MONTH(tanggal) = '{month}' AND parameter = 'debit'"
        result = connection(query, 'select')
        return result