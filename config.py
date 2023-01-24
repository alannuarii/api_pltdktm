import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    FILE_HIRARC = 'app/static/uploads/hirarc'
    