from flask import Flask, request

import remote
import models
import base64
import io
import utils
import json

app = Flask(__name__)


@app.route('/authorize', methods=['POST'])
def authorize():
    user = models.User(request)

    remote.authorize(user.username, user.password)
    buffer = utils.decode_img(user.image)
    utils.find_face(buffer)

    return json.dumps({'authorized': True, 'details': 'successfull'})


def decode_img(msg):
    msg = base64.b64decode(msg)
    buf = io.BytesIO(msg)
    return buf


if __name__ == '__main__':
    app.run()