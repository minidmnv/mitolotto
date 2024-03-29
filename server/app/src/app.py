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
    user = models.User(request.json['username'], request.json['password'], request.json['image'])
    result = False
    try:
        request_face_buffer = utils.decode_img(user.image)

        user_from_mock_api = remote.get_user_from_mock_remote_api(user.username)
        identity_document_buffer = utils.decode_img(user_from_mock_api.image)

        authorize_result = remote.authorize(user.password, user_from_mock_api.password)
        utils.find_face(request_face_buffer)
        compare_result = utils.compare_faces(identity_document_buffer, request_face_buffer)

        if compare_result and authorize_result:
            details = "login  successful"
            result = True
        else:
            details = "login failed"

    except Exception as exception:
        details = exception.args[0]

    return simplejson.dumps(models.AuthorizeResponse(str(result), details).__dict__)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
