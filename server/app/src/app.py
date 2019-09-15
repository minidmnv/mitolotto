import simplejson
from flask import Flask, request
from flask_cors import CORS

import models
import remote
import utils

app = Flask(__name__)
CORS(app)

@app.route('/authorize', methods=['POST'])
def authorize():
    user = models.User(request)
    result = False
    try:
        request_face_buffer = utils.decode_img(user.image)
        identity_document_buffer = utils.decode_img(remote.get_document(user.username))

        authorize_result = remote.authorize(user.username, user.password)
        utils.find_face(request_face_buffer)
        compare_result = utils.compare_faces(identity_document_buffer, request_face_buffer)

        if compare_result and authorize_result:
            details = "success"
            result = True
        else:
            details = "failed"

    except Exception as exception:
        details = exception.args[0]

    return simplejson.dumps(models.AuthorizeResponse(str(result), details).__dict__)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
