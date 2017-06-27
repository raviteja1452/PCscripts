import os
import time
import datetime
from py_scripts import start

threshold = 40

def auto_schedule():
    counter = 1
    while True:
        fp = open("./schedule_log.txt","a")
        t = str(datetime.datetime.now())
        fp.write("\n"+str(t)+"\n")
        r = int(os.popen("tmux ls | grep scrape- -c").read())
        # Priority
        if r < threshold:
            start.beginScraper(cId=2, wId=-1)
            #start.beginScraper(cId=16, wId=1)
            fp.write("\n\t started scraper for 2-- Total no of scrapers:"+str(r))


        r = int(os.popen("tmux ls | grep scrape- -c").read())
        # Others
        while r < threshold:
            if counter not in [45]:
                print counter
                start.beginScraper(cId=counter,wId=-1)
                fp.write("\n\t started scraper for "+str(counter)+" -- Total no of scrapers:"+str(r))
            counter = counter % 80 + 1
            r = int(os.popen("tmux ls | grep scrape- -c").read())
        fp.close()
        print "scrapers:",r
        time.sleep(3*60*60)


if __name__ == '__main__':
    auto_schedule()
