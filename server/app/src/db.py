from models import User
from utils import encode_img


def get_id(image):
    return encode_img("db/" + image + ".jpg")


class db:
    NGALDA = User('ngalda', 'ngalda_secret', get_id('ngalda'))
    MMORDA = User('mmorda', 'mmorda_secret', get_id('mmordalski'))
    SZWOJE = User('szwoj', 'szwoj_sercet', get_id('szwoj'))

    users = {NGALDA.username: NGALDA, MMORDA.username: MMORDA, SZWOJE.username: SZWOJE}
