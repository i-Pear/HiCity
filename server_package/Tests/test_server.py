import unittest
from hicityserver import *


class MyTestCase(unittest.TestCase):
    def test_config(self):
        from hicityserver.configuration import SQLALCHEMY_DATABASE_URI
        self.assertIsNotNone(SQLALCHEMY_DATABASE_URI)

    def test_database(self):
        init_db()
        from hicityserver.weather.model import WeatherRecord
        self.assertIsNotNone(WeatherRecord.query.all())


if __name__ == '__main__':
    unittest.main()
