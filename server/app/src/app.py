import simplejson
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

    try:
        found_face = utils.find_face(buffer)
        if found_face:
            details = 'successfull'
        else:
            details = 'unsuccessfull'

    except Exception as exception:
        found_face = False
        details = type(exception).__name__

    return simplejson.dumps(models.AuthorizeResponse(found_face, details).__dict__)


if __name__ == '__main__':
    app.run()
