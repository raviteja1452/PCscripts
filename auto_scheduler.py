import os
import time
import datetime
from py_scripts import start

threshold = 80

def auto_schedule():
    #fp = open("schedule_log.txt","a")
    counter = 1
    while True:
	fp = open("./schedule_log.txt","a")
        t = str(datetime.datetime.now())
        fp.write('\n'+str(t)+'\n')
        r = int(os.popen('tmux ls | grep scrape- -c').read())
        # Priority
        if r < threshold:
            start.beginScraper(cId=2, wId=-1)
            start.beginScraper(cId=3, wId=-1)
            start.beginScraper(cId=16, wId=-1)
            fp.write('\n\t started scraper for 2,3 and 16 -- Total no of scrapers:'+str(r))


        r = int(os.popen('tmux ls | grep scrape- -c').read())
        # Others
        while r < threshold:
            if counter not in [2,3,16]:
                start.beginScraper(cId=counter,wId=-1)
                fp.write('\n\t started scraper for '+str(counter)+' -- Total no of scrapers:'+str(r))
            counter = counter % 44 + 1
            r = int(os.popen('tmux ls | grep scrape- -c').read())
	fp.close()
	print 'scrapers:',r
        time.sleep(3*60*60)


if __name__ == '__main__':
    auto_schedule()
