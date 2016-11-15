sudo cd ~
sudo  curl -L "https://github.com/docker/compose/releases/download/1.8.1/docker-compose-$(uname -s)-$(uname -m)" > ./docker-compose
sudo cp ./docker-compose /usr/local/bin/docker-compose
cd ~
rm -r ./docker-compose
chmod +x /usr/local/bin/docker-compose
docker-compose --version

sudo cd ~
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo pip install cookiecutter
cookiecutter gh:TeamHG-Memex/aquarium
cd ./aquarium
sudo docker-compose up