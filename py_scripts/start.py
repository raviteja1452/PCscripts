import os
import sys
import time
import getopt


def beginScraper(cId, wId=-1):

    ts = "tmux new-session -d -s scrape-<cId>_<wId> './shell_scripts/<file>.sh'\n\n"
    st = """cd /home/neelendra/PCScraper2\n"""
    st += """source /home/neelendra/PCScraper2/scraperservice/bin/activate\n"""
    st += """PYTHONPATH=/home/neelendra/PCScraper2 python /home/neelendra/PCScraper2/scheduler/scrape.py -w <wId> -c <cId>\n"""

    st = st.replace('<cId>', str(cId))

    ts = ts.replace('<cId>', str(cId))

    fn = "scrape-<cId>_<wId>"

    w = open('./shell_scripts/start.sh', 'w')
    w.write('')
    w.close()
    if wId == -1:
        for i in range(1, 2):
            fns = fn.replace('<wId>', str(i)).replace('<cId>', str(cId))
            f = open('./shell_scripts/' + fns + '.sh', 'w')
            stc = st.replace('<wId>', str(i))
            f.write(stc)
            f.close()
            w = open('./shell_scripts/start.sh', 'a')
            tsc = ts.replace('<wId>', str(i)).replace('<file>', fns)
            w.write(tsc)
            w.close()
    else:
	print wId,cId
        fn.replace('<wId>', str(wId)).replace('<cId>', str(cId))
        f = open('./shell_scripts/' + fn + '.sh', 'w')
        st = st.replace('<wId>', str(wId));
        f.write(st)
        f.close()
        w = open('./shell_scripts/start.sh', 'a')
        tsc = ts.replace('<wId>', str(wId)).replace('<file>', fn)
        tsc = ts.replace('<wId>', str(wId)).replace('<file>', fn)
	print tsc
	w.write(tsc)
        w.close()
    os.system('chmod -R 777 ./shell_scripts')
    os.system('./shell_scripts/start.sh')
    time.sleep(5)
# if __name__ == '__main__':
#     argv = sys.argv[1:]
#     wId = -1
#     cId = -1
# try:
#     opts, args = getopt.getopt(argv, "hw:c:", ["websiteId=", "categoryId="])
# except getopt.GetoptError as e:
#     print 'begin.py getoptError:', e
#     sys.exit(2)
# for opt, arg in opts:
#     if opt == '-h':
#         print 'Main.py -w <websiteId> -c <categoryId>'
#         sys.exit(2)
#     elif opt in ("-w", "--websiteId"):
#         wId = arg
#     elif opt in ("-c", "--categoryId"):
#         cId = arg
# if cId == -1:
#     print "Enter category id (mandatory field)"
# else:
#     beginScraper(wId=wId, cId=cId)

