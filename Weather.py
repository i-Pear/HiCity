import gzip

import requests


class Weather:

    def __init__(self, json=None):
        if json is not None:
            self.cityName = json['city']
            self.ganmao = json['ganmao']
            self.date = json['forecast'][0]['date']
            self.high = json['forecast'][0]['high'].split()[1]
            self.low = json['forecast'][0]['low'].split()[1]
            self.wind = json['forecast'][0]['fengli'][9:13]
            self.type = json['forecast'][0]['type']


def getWeather(code: int):
    kw = {'citykey': code}
    response = requests.get("http://wthrcdn.etouch.cn/weather_mini?", params=kw).json()
    if response['status'] != 1000:
        return Weather()
    return Weather(response['data'])


if __name__ == '__main__':
    weather = getWeather(101070101)
    print(weather.cityName)
