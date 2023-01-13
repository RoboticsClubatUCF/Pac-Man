#!/bin/bash
sudo docker pull mysql/mysql-server:latest # Pull latest docker container
sudo docker run -e MYSQL_ROOT_PASSWORD=PASSWORD -p 3306:3306 -d mysql/mysql-server:latest #startup container as a service