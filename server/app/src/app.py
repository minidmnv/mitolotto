from flask import Flask, request

import base64
import remote
import models
import base64
import io
import utils

app = Flask(__name__)


@app.route('/authorize', methods=['POST'])
def authorize():
    user = models.User(request)


    remote.authorize(user.username, user.password)
    utils.find_face(decode_img(user.image))

    return 'success!'


def decode_img(msg):
    # msg = msg[msg.find(b"<plain_txt_msg:img>")+len(b"<plain_txt_msg:img>"):
    #           msg.find(b"<!plain_txt_msg>")]
    msg = base64.b64decode(msg)
    buf = io.BytesIO(msg)
    return buf


if __name__ == '__main__':
    app.run()