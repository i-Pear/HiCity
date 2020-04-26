import unittest
from hicity import HiCity


class MyTestCase(unittest.TestCase):
    def test_functions(self):
        app=HiCity()
        app.loadFullData()
        app.query('沈阳')
        app.query('沈阳1')
        app.query('abc')


if __name__ == '__main__':
    unittest.main()
