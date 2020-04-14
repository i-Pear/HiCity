from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/weather', methods=['GET'])
def getWeather():
    p = request.args.get('p')
    type = request.args.get('type')


if __name__ == '__main__':
    app.run()
