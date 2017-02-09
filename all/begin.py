import os
import sys
import getopt


def beginScraper(wId, cId):
    ts = "tmux new-session -d -s <wId>-<cId> './create.sh'"
    st = """ cd /home/pc/PCScraper\n"""
    st += """source /home/pc/PCScraper/scraperservice/bin/activate\n"""
    st += """PYTHONPATH=/home/pc/PCScraper python /home/pc/PCScraper/scheduler/Main.py -w <wId> -c <cId>\n"""
    st += """cd ~/PCscripts\n"""
    st += """./end_script.sh\n"""
    st = st.replace('<cId>', cId);
    ts = ts.replace('<cId>', cId);
    
    if wId == -1:
        for i in range(1,11):
            f = open('create.sh', 'w')
            stc = st.replace('<wId>', i);
            f.write(stc)
            f.close()
            tsc = ts.replace('<wId>', i);
            os.system(tsc)
    else
        f = open('create.sh', 'w')
        st = st.replace('<wId>', wId);
        f.write(st)
        f.close()
        ts = ts.replace('<wId>', wId);
        os.system(ts)


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
