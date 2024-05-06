#!/usr/bin/env bash
# Script sets up a seb server for the deplyiment of web_static
#install nginx
sudo apt update
sudo apt-get install -y nginx
#create directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/current/index.html

#create symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current
#change the ownere of the directory
sudo chown -R ubunt:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/we_static/current/;}' /etc/nginx/sites-available/default
