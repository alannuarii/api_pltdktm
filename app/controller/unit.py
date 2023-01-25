from db import connection

class Unit:
    def get_all_by_id(self, id):
        query = f"SELECT id_unit, u.bahan_bakar, u.tahun_operasi, u.dtp, u.dmn, e.pabrik 'ePabrik', e.tipe 'eTipe', e.tahun_pembuatan 'eTahunPembuatan', e.daya_nominal 'eDayaNominal', e.putaran 'ePutaran', e.nomor_seri 'eNomorSeri', g.pabrik 'gPabrik', g.tipe 'gTipe', g.tahun_pembuatan 'gTahunPembuatan', g.nomor_seri 'gNomorSeri', g.daya_nominal 'gDayaNominal', g.tegangan 'gTegangan', g.arus 'gArus', g.putaran 'gPutaran', g.frekuensi 'gFrekuensi', g.tegangan_eksitasi 'gTeganganEksitasi', g.arus_eksitasi 'gArusEksitasi', g.jumlah_fasa 'gJumlahFasa', g.faktor_daya 'gFaktorDaya', t.pabrik 'tPabrik', t.tipe 'tTipe', t.tahun_pembuatan 'tTahunPembuatan', t.nomor_seri 'tNomorSeri', t.sistem_pendingin 'tSistemPendingin', t.jumlah_fasa 'tJumlahFasa', t.kapasitas_terpasang 'tKapasitasTerpasang', t.tegangan_HV 'tTeganganHV', t.tegangan_LV 'tTeganganLV', t.arus_HV 'tArusHV', t.arus_LV 'tArusLV', t.jumlah_tap 'tJumlahTap', t.frekuensi 'tFrekuensi', t.kelompok_vektor 'tKelompokVektor', t.impedansi 'tImpedansi' FROM unit AS u JOIN engine AS e ON u.id_unit = e.unit_id JOIN generator AS g ON u.id_unit = g.unit_id JOIN trafo AS t ON u.id_unit = t.unit_id WHERE id_unit = {id}"
        result = connection(query, 'select')
        return result


