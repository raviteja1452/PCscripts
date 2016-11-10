cd /home/ubuntu/PCScraper/scrapperservice
source /home/ubuntu/PCScraper/scrapperservice/scrapperservice/bin/activate

PYTHONPATH=/home/ubuntu/PCScraper/scrapperservice python /home/ubuntu/PCScraper/scrapperservice/scheduler/Main.py -c 4 -w 4
