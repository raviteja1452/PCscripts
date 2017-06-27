import os
import time
import datetime
from py_scripts import refresh_start

threshold = 10


def refresh_schedule():
    counter = 1
    while True:
        fp = open("./refresh_log.txt", "a")
        t = str(datetime.datetime.now())
        fp.write("\n" + str(t) + "\n")
        r = int(os.popen("tmux ls | grep refresh- -c").read())
        # Priority
        if r < threshold:
            refresh_start.beginScraper(cId=2)
            fp.write("\n\t started refresher for 2-- Total no of refreshers:" + str(r))

        r = int(os.popen("tmux ls | grep refresh- -c").read())
        # Others
        while r < threshold:
            if counter not in [45]:
                print counter
                refresh_start.beginScraper(cId=counter)
                fp.write("\n\t started refresher for " + str(counter) + " -- Total no of refreshers:" + str(r))
            counter = counter % 80 + 1
            r = int(os.popen("tmux ls | grep refresh- -c").read())
        fp.close()
        print "refreshers:", r
        time.sleep(3 * 60 * 60)


if __name__ == '__main__':
    refresh_schedule()
