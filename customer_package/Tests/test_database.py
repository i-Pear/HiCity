import unittest
from hicity import HiCity


class MyTestCase(unittest.TestCase):
    def test_loadDataFromExt(self):
        app = HiCity()
        app.db.loadDataFromExternal(silent=True)
        self.assertNotEqual(len(app.db.getCitiesAll()), 0)

    def test_detele(self):
        app = HiCity()
        l = len(app.db.getCitiesAll())
        app.db.deleteCity(app.db.getCitiesAll()[0])
        self.assertEqual(l - 1, len(app.db.getCitiesAll()))

    def test_export(self):
        app=HiCity()
        app.db.backupDataToExcel('test')
        self.assertIsNotNone(open('test.xls'))


if __name__ == '__main__':
    unittest.main()
