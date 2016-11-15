sudo cd ~
sudo  curl -L "https://github.com/docker/compose/releases/download/1.8.1/docker-compose-$(uname -s)-$(uname -m)" > ./docker-compose
sudo cp ./docker-compose /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
docker-compose --version

sudo cd ~
sudo pip install cookiecutter
cookiecutter gh:TeamHG-Memex/aquarium
cd ./aquarium
sudo docker-compose up