import os
import time
import datetime
from py_scripts import start

threshold = 80

def auto_schedule():
    fp = open("schedule_log.txt","a")
    counter = 1
    while True:
        t = str(datetime.datetime.now())
        fp.write(t);
        r = int(os.popen('tmux ls | grep scrape- -c').read())
        # Priority
        if r < threshold:
            start.beginScraper(cId=2, wId=-1)
            start.beginScraper(cId=3, wId=-1)
            start.beginScraper(cId=16, wId=-1)
            fp.write('\t started scraper for 2,3 and 16')


        r = int(os.popen('tmux ls | grep scrape- -c').read())
        # Others
        while r < threshold:
            if counter not in [2,3,16]:
                start.beginScraper(cId=counter,wid=-1)
                fp.write('\t started scraper for '+counter)
            counter = counter % 44 + 1
            r = int(os.popen('tmux ls | grep scrape- -c').read())

        time.sleep(3*60*60)


if __name__ == '__main__':
    auto_schedule()
