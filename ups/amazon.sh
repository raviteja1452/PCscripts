cd /home/neelendra/PCScraper
source /home/neelendra/PCScraper/scraperservice/bin/activate

PYTHONPATH=/home/neelendra/PCScraper python /home/neelendra/PCScraper/scheduler/Main.py -c 22 -w 1
cd ~/PCscripts
./end_script.sh
