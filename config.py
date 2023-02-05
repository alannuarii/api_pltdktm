import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    FILE_HIRARC = 'app/static/uploads/hirarc'
    FILE_JSA = 'app/static/uploads/jsa'
    FILE_PROSEDUR = 'app/static/uploads/prosedur'
    FILE_SERTIFIKAT = 'app/static/uploads/sertifikat'
    FOTO_PRESENSI = 'app/static/uploads/presensi'
    