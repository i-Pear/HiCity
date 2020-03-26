import argparse
import difflib
from prompt_toolkit import prompt
from AutoComplete import CNameCompleter
import logging
from DataControl import DataControl


class HiCity:
    """
    A module for fast querying codes of cities
    """
    citiesCache = {}

    def __init__(self):
        """
        Load city code data
        """
        self.completer = CNameCompleter(self.citiesCache.keys())
        self.db = DataControl()
        self._allDataLoaded = False

    def loadFullData(self):
        """
        Load all data from database to build-in cache dict
        for functions which needs frequently reading
        """
        if self._allDataLoaded:
            return
        self._allDataLoaded = True
        for city in self.db.getCitiesAll():
            if city.name not in self.citiesCache.keys():
                self.citiesCache[city.name] = [city.code]
            else:
                self.citiesCache[city.name].append(city.code)

    def query(self, cname: str):
        """
        query
        :return: query result as string
        """
        logging.info('user queried ' + cname)
        if cname not in self.citiesCache.keys():
            similar = self.find_similar(cname)
            if len(similar) > 0:
                return 'City not found! ' + 'Did you mean:\n' + ','.join(similar)
            else:
                return 'City not found!\n'
        else:
            if len(self.citiesCache[cname]) == 1:
                message = 'The code of ' + cname + ' is ' + self.citiesCache[cname][0]
                logging.info(message)
                return message
            else:
                message = 'There are' + str(len(self.citiesCache[cname])) + 'cities with the same name:'
                for code in self.citiesCache[cname]:
                    message = message + '\n' + code
                return message

    def find_similar(self, text):
        self.loadFullData()
        return difflib.get_close_matches(text, self.citiesCache.keys())

    def find(self, text):
        # search_result = [item for item in self.citiesCache.keys() if item.find(text) != -1]
        search_result = self.db.getCitiesByName('%{0}%'.format(text))
        if len(search_result) != 0:
            return '\n'.join([city.name for city in search_result])
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
    parser.add_argument('-backup', type=str, help='export data to a excel file')
    parser.add_argument('-createDB', action='store_true', help='initial database from text file')
    return parser.parse_args()


version = 'HiCity v0.3'

if __name__ == '__main__':
    args = get_args()
    if not args.ver and not args.query and not args.i and not args.find:
        print('Invalid argument. Type HiCity --help to see help')

    if args.ver:
        print(version)

    elif args.query:
        hiCity = HiCity()
        print(hiCity.query(args.query))

    elif args.find:
        hiCity = HiCity()
        print(hiCity.find(args.find))

    elif args.i:
        hiCity = HiCity()
        hiCity.interact()

    elif args.createDB:
        hiCity = HiCity()
        hiCity.db.loadDataFromExternal(dataPath=args.data)

    elif args.backup:
        hiCity = HiCity()
        hiCity.db.backupDataToExcel(args.backup)
