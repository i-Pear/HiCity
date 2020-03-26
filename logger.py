import sys
import time
import traceback


class Logger:
    def __init__(self):
        self.writer = open('log.txt', 'a')

    def __call__(self, item):
        print(time.asctime(time.localtime(time.time())), item, file=self.writer)

    def __del__(self):
        self.writer.close()


log = Logger()

if __name__ == '__main__':
    # unit test
    log('Testing logger output')
