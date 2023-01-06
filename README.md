# Pac-Man

Pac-Man is a straightforward and easy to use Django handled search / inventory system.

## Running the Server

python ./manage.py runserver

### Oh NO! ive run into errors

run

## Installation

reqs
    python >= 3.9
    python libs :
        django
        mysqlclient
    mysql db [https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04]

### Step by Step

if you want a different password for the database, change it in the etc/mysql dir

install  the python libs
install mysql n stuff
log into mysql
run the following commands
    CREATE USER 'roboticsuser'@'localhost' IDENTIFIED BY 'pwd';
    CREATE DATABASE robotics_inv;
    GRANT ALL PRIVILEGES ON *.* TO 'roboticsuser'@'localhost' WITH GRANT OPTION;
    GRANT ALL ON * TO 'roboticsuser'@'localhost';
    FLUSH PRIVILEGES;
    exit

aight now migrate all the stuff

run these things
    python(VERSION) ./manage.py createsuperuser # this makes a super user that can access the admin panel at localhost:8000/admin
    python(VERSION) ./manage.py makemigrations
    python(VERSION) ./manage.py makemigrations inventory
    python(VERSION) ./manage.py migrate

now you can finally run the server!

    python(VERSION) ./manage.py runserver
