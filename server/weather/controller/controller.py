from ..model import WeatherRecord
import datetime
import requests
from flask import request
from .. import app, db


@app.route('/')
def hello_world():
    return 'Service running...'


@app.route('/weather', methods=['GET'])
def getWeather():
    code = request.args.get('id')
    now = datetime.datetime.now()
    timestamp = '{0}-{1}-{2}'.format(now.year, now.month, now.day)

    response = requests.get("http://wthrcdn.etouch.cn/weather_mini?",
                            params={'citykey': code}).json()
    return response
