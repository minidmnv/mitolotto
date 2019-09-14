import simplejson
from flask import Flask, request

import models
import remote
import utils

app = Flask(__name__)


@app.route('/authorize', methods=['POST'])
def authorize():
    user = models.User(request)

    try:
        request_face_buffer = utils.decode_img(user.image)
        identity_document_buffer = utils.decode_img(remote.get_document(user.username))

        remote.authorize(user.username, user.password)
        utils.find_face(request_face_buffer)
        authorize_result = utils.compare_faces(identity_document_buffer, request_face_buffer)

        if authorize_result:
            details = "authorization succeeded"
        else:
            details = "authorization failed"

    except Exception as exception:
        authorize_result = False
        details = type(exception).__name__

    return simplejson.dumps(models.AuthorizeResponse(str(authorize_result), details).__dict__)


if __name__ == '__main__':
    app.run()
