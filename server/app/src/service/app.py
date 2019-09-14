from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def helloIndex():
    return 'Hello HackYeah!'

if __name__ == '__main__':
    app.run()