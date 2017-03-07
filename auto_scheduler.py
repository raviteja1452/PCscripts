import os
from py_scripts import start


def auto_schedule():
    r = int(os.popen('tmux ls | grep scrape -c').read())
    print r
    start.beginScraper(cId=20, wId=-1)


if __name__ == '__main__':
    auto_schedule()
