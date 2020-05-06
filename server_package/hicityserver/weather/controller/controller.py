from ..model import WeatherRecord
import datetime
import time
import requests
from flask import request, render_template
from .. import app, db
import json
from multiprocessing import Process


def heavyLoad():
    time.sleep(10)
    print('slept 10s')


@app.route('/')
def hello():
    Process(target=heavyLoad).start()
    return render_template('index.html')


@app.route('/weather', methods=['GET'])
def getWeather():
    code = request.args.get('id')
    timestamp = request.args.get('time')
    now = datetime.datetime.now()
    today = '{0}-{1}-{2}'.format(now.year, now.month, now.day)

    if code is None:
        return 'id segment is empty!'
    if timestamp is None:
        timestamp = today

    cache = WeatherRecord.query.filter(WeatherRecord.id == code, WeatherRecord.time == timestamp).first()
    if cache is not None:
        print('Using cached data.')
        return json.loads(cache.data)
    else:
        if timestamp != today:
            return 'history data not found!'
        print('Fetching new data...')
        response = requests.get("http://wthrcdn.etouch.cn/weather_mini?",
                                params={'citykey': code}).json()
        data = WeatherRecord(id=code, time=timestamp, data=json.dumps(response))
        db.session.add(data)
        db.session.commit()
        return response


@app.route('/weather', methods=['POST'])
def updateWeather():
    code = request.args.get('id')
    now = datetime.datetime.now()
    timestamp = '{0}-{1}-{2}'.format(now.year, now.month, now.day)
    cache = WeatherRecord.query.filter(WeatherRecord.id == code, WeatherRecord.time == timestamp).first()
    if cache is not None:
        db.session.delete(cache)

    response = requests.get("http://wthrcdn.etouch.cn/weather_mini?",
                            params={'citykey': code}).json()
    data = WeatherRecord(id=code, time=timestamp, data=json.dumps(response))
    db.session.add(data)
    db.session.commit()
    return response
