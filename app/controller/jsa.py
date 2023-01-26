from db import connection
from flask import request

class JSA:
    def upload_jsa(self):
        tahap_pekerjaan = request.form.getlist('tahap_pekerjaan')
        potensi_risiko = request.form.getlist('potensi_risiko')
        pengendalian_risiko = request.form.getlist('pengendalian_risiko')
        wp_id = request.form['wp_id']

        for i in range(len(tahap_pekerjaan)):
            self.insert_jsa(tahap_pekerjaan[i], potensi_risiko[i], pengendalian_risiko[i], wp_id)

    def insert_jsa(self, tahap_pekerjaan, potensi_risiko, pengendalian_risiko, wp_id):
        query = f"INSERT INTO jsa (tahap_pekerjaan, potensi_risiko, pengendalian_risiko, wp_id) VALUES ('{tahap_pekerjaan}', '{potensi_risiko}', '{pengendalian_risiko}', {wp_id})"
        connection(query, 'insert')