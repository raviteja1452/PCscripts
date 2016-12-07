cd /home/ubuntu/PCScraper/scrapperservice
source /home/ubuntu/PCScraper/scrapperservice/scrapperservice/bin/activate

PYTHONPATH=/home/ubuntu/PCScraper/scrapperservice python /home/ubuntu/PCScraper/scrapperservice/scheduler/Main.py -c 38 -w 2
cd ~/PCscripts
./end_script.sh