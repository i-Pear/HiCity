import os
import sys
import time

import xlwt
from prompt_toolkit.shortcuts import ProgressBar
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging


def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("..")

    return os.path.join(base_path, relative_path)


MyBase = declarative_base()


class City(MyBase):
    __tablename__ = "city"
    code = Column(Integer, primary_key=True)
    name = Column(VARCHAR(10))

    def __repr__(self):
        return "[City(name='{1}', code='{0}')]".format(self.code, self.name)


class DataControl:
    def __init__(self):
        self.engine = create_engine('sqlite:///data.db')
        MyBase.metadata.create_all(self.engine, checkfirst=True)
        self.session = self.Session = sessionmaker(bind=self.engine)()

    def addCity(self, code: int, cname: str):
        newItem = City(code=code, name=cname)
        self.session.add(newItem)
        self.session.commit()

    def addCities(self, cities):
        self.session.add_all(cities)
        self.session.commit()

    def deleteCity(self, city: City):
        self.session.delete(city)
        self.session.commit()

    def getCitiesAll(self):
        return self.session.query(City).all()

    def getCitiesByCode(self, code: int):
        return self.session.query(City).filter_by(code=code).all()

    def getCitiesByName(self, name: str):
        return self.session.query(City).filter_by(name=name).all()

    def findCitiesByName(self, name: str):
        return self.session.query(City).filter(City.name.like('%{0}%'.format(name))).all()

    def backupDataToExcel(self, filename):
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('CityData')
        cities = self.getCitiesAll()
        for row, city in enumerate(cities):
            sheet.write(row, 0, city.name)
            sheet.write(row, 1, city.code)
        workbook.save(filename+'.xls')
        print('Saved {0} records to excel file.'.format(len(cities)))

    def loadDataFromExternal(self, dataPath: str = 'citycode.data', silent=False):
        self.session.query(City).delete()
        logging.info('Database cleared.')

        with open(resource_path(dataPath), 'r', encoding='UTF-8') as reader:
            logging.info('Started loading data...')
            totalRecord = int(reader.readline())
            cities = []
            if not silent:
                with ProgressBar() as pb:
                    label = 'Loading data'
                    bar = pb(range(1, totalRecord + 1), label=label)
                    for cntRecord in bar:
                        time.sleep(0.0001)  # delay for display effects
                        line = reader.readline()
                        sp = line.strip().split(',')  # 去除行尾换行并分割
                        if len(sp) != 2:
                            continue  # 处理异常数据
                        cities.append(City(code=int(sp[1]), name=sp[0]))
            else:
                for cntRecord in range(1, totalRecord + 1):
                    line = reader.readline()
                    sp = line.strip().split(',')  # 去除行尾换行并分割
                    if len(sp) != 2:
                        continue  # 处理异常数据
                    cities.append(City(code=int(sp[1]), name=sp[0]))
            self.addCities(cities)

            print('Data loaded successfully.\n')
            logging.info('Data loaded successfully.')

    def commit(self):
        self.session.commit()
