from flask import Flask, request

import base64
import remote
import models

app = Flask(__name__)


@app.route('/authorize', methods=['POST'])
def authorize():
    user = models.User(request)


    remote.authorize(user.username, user.password)

    filename = 'tmp_image.jpg'
    with open(filename, 'wb') as f:
        f.write(base64.b64decode(photo))

    return 'success!'


if __name__ == '__main__':
    app.run()