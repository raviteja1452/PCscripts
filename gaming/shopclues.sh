cd /home/pc/PCScraper
source /home/pc/PCScraper/scraperservice/bin/activate

PYTHONPATH=/home/pc/PCScraper python /home/pc/PCScraper/scheduler/Main.py -c 34 -w 5
./end_script.sh
