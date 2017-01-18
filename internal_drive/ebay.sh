cd /home/pc/PCScraper
source /home/pc/PCScraper/scraperservice/bin/activate

PYTHONPATH=/home/pc/PCScraper pypy /home/pc/PCScraper/scheduler/Main.py -c 30 -w 7
cd ~/PCscripts
./end_script.sh
