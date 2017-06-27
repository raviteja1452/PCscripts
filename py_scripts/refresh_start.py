import os
import time


def beginScraper(cId):
    ts = """tmux new-session -d -s refresh-<cId> './shell_scripts/<file>.sh'\n\n"""

    st = """cd /home/neelendra/PCScraper2\n"""
    st += """source /home/neelendra/PCScraper2/scraperservice/bin/activate\n"""
    st += """PYTHONPATH=/home/neelendra/PCScraper2 python /home/neelendra/PCScraper2/scheduler/product_refresher.py -c <cId>\n"""

    fn = "refresh-<cId>"

    st = st.replace("<cId>", str(cId))

    ts = ts.replace("<cId>", str(cId))

    fn = fn.replace("<cId>", str(cId))

    f = open("./shell_scripts/" + fn + ".sh", "w")
    f.write(st)
    f.close()

    w = open("./shell_scripts/refresh_start.sh", "a")
    tsc = ts.replace("<file>", fn)
    w.write(tsc)
    w.close()

    os.system("chmod -R 777 ./shell_scripts")
    os.system("./shell_scripts/refresh_start.sh")
    time.sleep(5)

