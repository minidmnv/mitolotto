import json

from flask import Flask, request

import models
import remote
import utils

app = Flask(__name__)


@app.route('/authorize', methods=['POST'])
def authorize():
    user = models.User(request)

    remote.authorize(user.username, user.password)
    buffer = utils.decode_img(user.image)
    utils.find_face(buffer)

    return json.dumps({'authorized': True, 'details': 'successfull'})


if __name__ == '__main__':
    app.run()
