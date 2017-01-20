cd /home/pc/PCScraper
source /home/pc/PCScraper/scraperservice/bin/activate

PYTHONPATH=/home/pc/PCScraper python /home/pc/PCScraper/scheduler/Main.py -c 9 -w 1
cd ~/PCscripts
./end_script.sh
