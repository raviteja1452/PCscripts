sudo apt-get update
sudo apt-get install python
sudo apt-get install python-pip
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo pip install virtualenv

sudo apt-get install apt-transport-https ca-certificates
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" | sudo tee /etc/apt/sources.list.d/docker.list

sudo apt-get install linux-image-extra-$(uname -r) linux-image-extra-virtual
sudo apt-get update

sudo apt-get install docker-engine
sudo service docker start
sudo docker run hello-world
sudo pip install cookiecutter

sudo apt-get install libmysqlclient-dev
sudo apt-get install python-pip python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev
