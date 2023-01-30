import os
from app import app
from db import connection
from flask import request

class WP:
    def upload_file(self, file, type, id):
        if type == 'hirarc' and file.filename != 'undefined':
            renamefile = f"{type}{id}.pdf"
            file.save(os.path.join(app.config['FILE_HIRARC'], renamefile))
            return renamefile
        elif type == 'jsa' and file.filename != 'undefined':
            renamefile = f"{type}{id}.pdf"
            file.save(os.path.join(app.config['FILE_JSA'], renamefile))
            return renamefile
        elif type == 'prosedur_kerja' and file.filename != 'undefined':
            renamefile = f"{type}{id}.pdf"
            file.save(os.path.join(app.config['FILE_PROSEDUR'], renamefile))
            return renamefile
        elif type == 'sertifikat' and file.filename != 'undefined':
            renamefile = f"{type}{id}.pdf"
            file.save(os.path.join(app.config['FILE_SERTIFIKAT'], renamefile))
            return renamefile
        else:
            return ''

    def get_wp(self):
        query = f"SELECT * FROM wp"
        result = connection(query, 'select')
        return result

    def get_wp_id(self, id):
        query = f"SELECT * FROM wp WHERE id_wp = {id}"
        result = connection(query, 'select')
        return result

    def insert_wp(self, id_wp, tanggal_pengajuan, nama_pekerjaan, detail_pekerjaan, lokasi_pekerjaan, pengawas_pekerjaan, pengawas_k3, tanggal_mulai, tanggal_selesai, klasifikasi_pekerjaan, klasifikasi_lainnya, prosedur_pekerjaan, prosedur_lainnya, hirarc, jsa, prosedur_kerja, sertifikat):
        query = f"INSERT INTO wp (id_wp, tanggal_pengajuan, nama_pekerjaan, detail_pekerjaan, lokasi_pekerjaan, pengawas_pekerjaan, pengawas_k3, tanggal_mulai, tanggal_selesai, klasifikasi_pekerjaan, klasifikasi_lainnya, prosedur_pekerjaan, prosedur_lainnya, hirarc, jsa, prosedur_kerja, sertifikat) VALUES ({id_wp}, '{tanggal_pengajuan}', '{nama_pekerjaan}', '{detail_pekerjaan}', '{lokasi_pekerjaan}', '{pengawas_pekerjaan}', '{pengawas_k3}', '{tanggal_mulai}', '{tanggal_selesai}', '{klasifikasi_pekerjaan}', '{klasifikasi_lainnya}', '{prosedur_pekerjaan}', '{prosedur_lainnya}', '{hirarc}', '{jsa}', '{prosedur_kerja}', '{sertifikat}')"
        connection(query, 'insert')

    def upload_wp(self):
        id_wp = request.form['id_wp']
        tanggal_pengajuan = request.form['tanggal_pengajuan']
        nama_pekerjaan = request.form['nama_pekerjaan']
        detail_pekerjaan = request.form['detail_pekerjaan']
        lokasi_pekerjaan = request.form['lokasi_pekerjaan']
        pengawas_pekerjaan = request.form['pengawas_pekerjaan']
        pengawas_k3 = request.form['pengawas_k3']
        tanggal_mulai = request.form['tanggal_mulai']
        tanggal_selesai = request.form['tanggal_selesai']
        klasifikasi_pekerjaan = request.form['klasifikasi_pekerjaan']
        klasifikasi_lainnya = request.form['klasifikasi_lainnya']
        prosedur_pekerjaan = request.form['prosedur_pekerjaan']
        prosedur_lainnya = request.form['prosedur_lainnya']
        hirarc = request.files['hirarc']
        jsa = request.files['jsa']
        prosedur_kerja = request.files['prosedur_kerja']
        sertifikat = request.files['sertifikat']

        self.insert_wp(id_wp, tanggal_pengajuan, nama_pekerjaan, detail_pekerjaan, lokasi_pekerjaan, pengawas_pekerjaan, pengawas_k3,
         tanggal_mulai, tanggal_selesai, klasifikasi_pekerjaan, klasifikasi_lainnya, prosedur_pekerjaan, prosedur_lainnya, self.upload_file(hirarc, 'hirarc', id_wp), self.upload_file(jsa, 'jsa', id_wp), self.upload_file(prosedur_kerja, 'prosedur_kerja', id_wp), self.upload_file(sertifikat, 'sertifikat', id_wp))
        




