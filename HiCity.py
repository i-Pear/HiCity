import os
import sys
import time
import argparse
import difflib
from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import ProgressBar

from AutoComplete import CNameCompleter
from logger import log


def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class HiCity:
    """
    A module for fast querying codes of cities
    """
    cities = {}

    def __init__(self, dataPath, silent=False):
        """
        Load city code data
        """
        with open(resource_path(dataPath), 'r', encoding='UTF-8') as reader:
            log('Started loading data...')
            totalRecord = int(reader.readline())
            with ProgressBar() as pb:
                if not silent:
                    label = 'Loading data'
                    bar = pb(range(1, totalRecord + 1), label=label)
                else:
                    bar = range(1, totalRecord + 1)
                for cntRecord in bar:
                    if not silent:
                        time.sleep(0.0001)  # delay for display effects
                    line = reader.readline()
                    sp = line.strip().split(',')  # 去除行尾换行并分割
                    if len(sp) != 2:
                        continue  # 处理异常数据
                    if sp[0] in self.cities.keys():  # 如果有重名
                        self.cities[sp[0]].append(sp[1])
                    else:
                        self.cities[sp[0]] = [sp[1]]
                if not silent:
                    print('Data loaded successfully.\n')
                log('Data loaded successfully.')

        self.completer = CNameCompleter(self.cities.keys())

    def query(self, cname: str):
        """
        query
        :return: query result as string
        """
        log('user queried ' + cname)
        if cname not in self.cities.keys():
            log('City not found!\n')
            similar = self.find_similar(cname)
            if len(similar) > 0:
                return 'City not found! ' + 'Did you mean:\n' + ','.join(similar)
            else:
                return 'City not found!\n'
        else:
            if len(self.cities[cname]) == 1:
                message = 'The code of ' + cname + ' is ' + self.cities[cname][0]
                log(message)
                return message
            else:
                message = 'There are' + str(len(self.cities[cname])) + 'cities with the same name:'
                for code in self.cities[cname]:
                    message = message + '\n' + code
                log(message)
                return message

    def find_similar(self, text):
        return difflib.get_close_matches(text, self.cities.keys())

    def find(self, text):
        search_result = [item for item in self.cities.keys() if item.find(text) != -1]
        if len(search_result) != 0:
            return '\n'.join(search_result)
        else:
            return self.query(text)

    def interact(self):
        # autoComplete = AutoComplete(self.get_completion)
        print('Any time you can enter "-" to exit')
        while True:
            cname = prompt('Enter city name:\n', completer=self.completer,
                           complete_while_typing=True)
            if cname == '-':
                return
            print(self.query(cname))
            print('')  # print a blank line


def get_args():
    parser = argparse.ArgumentParser(description='HiCity Agent')
    parser.add_argument('-data', type=str, default='citycode.data', help='location of the city code data')
    parser.add_argument('-query', type=str, default='', help='city name to query')
    parser.add_argument('-ver', action='store_true', help='show version')
    parser.add_argument('-find', type=str, help='find cities with substring')
    parser.add_argument('-i', action='store_true', help='show interactive interface')
    args = parser.parse_args()
    return args


version = 'HiCity v0.2'

if __name__ == '__main__':
    args = get_args()
    if not args.ver and not args.query and not args.i and not args.find:
        print('Invalid argument. Type HiCity --help to see help')

    if args.ver:
        print(version)

    if args.query:
        hiCity = HiCity(args.data, silent=True)
        print(hiCity.query(args.query))
        args.i = False

    if args.find:
        hiCity = HiCity(args.data, silent=True)
        print(hiCity.find(args.find))
        args.i = False

    if args.i:
        hiCity = HiCity(args.data)
        hiCity.interact()
