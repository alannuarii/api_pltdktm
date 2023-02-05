import base64
from PIL import Image
from io import BytesIO


def base64topng(pic):
    picture = pic.replace('data:image/png;base64,', '')
    bytes_decoded = base64.b64decode(picture)
    photo = Image.open(BytesIO(bytes_decoded))
    return photo