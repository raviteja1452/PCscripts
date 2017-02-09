import os
import sys
import getopt


def stopScraper(wId, cId):
    ts = "tmux kill-session -t scrape-<wId>_<cId> \n\n"
    w = open('stop.sh', 'w')
    w.write('')
    w.close()
    ts.replace('<cId>', str(cId))
    if wId == -1:
        for i in range(1,11):
            w = open('stop.sh', 'a')
            tsc = ts.replace('<wId>', str(i))
            w.write(tsc)
            w.close()
    else:
        w = open('stop.sh', 'a')
        tsc = ts.replace('<wId>', wId)
        w.write(tsc)
        w.close()


if __name__ == '__main__':
    argv = sys.argv[1:]
    wId = -1
    cId = -1
try:
    opts, args = getopt.getopt(argv, "hw:c:", ["websiteId=", "categoryId="])
except getopt.GetoptError as e:
    print 'begin.py getoptError:', e
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print 'Main.py -w <websiteId> -c <categoryId>'
        sys.exit(2)
    elif opt in ("-w", "--websiteId"):
        wId = arg
    elif opt in ("-c", "--categoryId"):
        cId = arg
if cId == -1:
    print "Enter category id (mandatory field)"
else:
    stopScraper(wId=wId, cId=cId)
