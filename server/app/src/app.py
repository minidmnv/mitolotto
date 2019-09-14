from flask import Flask, request
import base64

app = Flask(__name__)


@app.route('/authorize', methods=['POST'])
def authorize():
    photo = request.json["photo"]
    username = request.json["username"]
    password = request.json["password"]
    filename = 'tmp_image.jpg'
    with open(filename, 'wb') as f:
        f.write(base64.b64decode(photo))

    return 'success!'


if __name__ == '__main__':
    app.run()