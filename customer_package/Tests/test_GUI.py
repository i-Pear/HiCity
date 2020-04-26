import unittest
from hicity import GUI


class MyTestCase(unittest.TestCase):
    def test_GUI(self):
        GUI()


if __name__ == '__main__':
    unittest.main()
