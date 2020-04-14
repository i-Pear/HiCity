from ..model import WeatherRecord
import datetime
import requests
from flask import request
from .. import app, db
import json


@app.route('/')
def hello_world():
    return 'Service running...'


@app.route('/weather', methods=['GET'])
def getWeather():
    code = request.args.get('id')
    now = datetime.datetime.now()
    timestamp = '{0}-{1}-{2}'.format(now.year, now.month, now.day)
    cache = WeatherRecord.query.filter(WeatherRecord.time == timestamp).first()
    if cache is not None:
        print('Using cached data.')
        return json.loads(cache.data)
    else:
        print('Fetching new data...')
        response = requests.get("http://wthrcdn.etouch.cn/weather_mini?",
                                params={'citykey': code}).json()
        data = WeatherRecord(time=timestamp, data=json.dumps(response))
        db.session.add(data)
        db.session.commit()
        return response
