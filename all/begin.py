import os
import sys
import getopt


def beginScraper(wId, cId):
    ts = "tmux new-session -d -s scrape-<wId>_<cId> './<file>.sh'\n\n"
    st = """cd /home/pc/PCScraper\n"""
    st += """source /home/pc/PCScraper/scraperservice/bin/activate\n"""
    st += """PYTHONPATH=/home/pc/PCScraper python /home/pc/PCScraper/scheduler/Main.py -w <wId> -c <cId>\n"""
    st += """cd ~/PCscripts\n"""
    st += """./end_script.sh\n\n\n"""
    st = st.replace('<cId>', cId);
    ts = ts.replace('<cId>', cId);
    fn = "scrape-<wId>_<cId>"
    w = open('start.sh', 'w')
    w.write('')
    w.close()
    if wId == -1:
        for i in range(1,11):
            fns = fn.replace('<wId>', str(i)).replace('<cId>',str(i))
            f = open(fns+'.sh', 'w')
            stc = st.replace('<wId>', str(i));
            f.write(stc)
            f.close()
            w = open('start.sh', 'a')
            tsc = ts.replace('<wId>', str(i)).replace('<file>',fns)
            w.write(tsc)
            w.close()
    else:
        fn.replace('<wId>', str(wId)).replace('<cId>',cId)
        f = open(fn+'.sh', 'w')
        st = st.replace('<wId>', wId);
        f.write(st)
        f.close()
        w = open('start.sh', 'a')
        tsc = ts.replace('<wId>', wId).replace('<file>',fn)
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
    beginScraper(wId=wId, cId=cId)
