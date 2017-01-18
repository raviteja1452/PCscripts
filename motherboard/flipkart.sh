cd /home/pc/PCScraper
source /home/pc/PCScraper/scraperservice/bin/activate

PYTHONPATH=/home/pc/PCScraper pypy /home/pc/PCScraper/scheduler/Main.py -c 26 -w 3
cd ~/PCscripts
./end_script.sh
