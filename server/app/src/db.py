from models import User
from utils import encode_img


def get_id(image):
    return encode_img("db/" + image + ".jpg")


class db:
    NGALDA = User('ngalda', 'ngalda_secret', get_id('gorgina'))
    MMORDA = User('mmorda', 'mmorda_secret', get_id('morda'))

    users = {NGALDA.username: NGALDA, MMORDA.username: MMORDA}
