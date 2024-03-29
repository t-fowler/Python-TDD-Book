Provisioning a new site
=======================

## Required packages:

* nginx
* Python3
* virtualenv + pip
* Git
  
eg, on Ubuntu:
sudo apt update
sudo apt install nginx git python3.10-venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, e.g., stagin.my-domain.com

## Systemd service

* see gunicorn-system.template.service
* replace DOMAIN with, e.g., staging.my-domain.com

## Folder structure:

Assume we have a user account at /home/username

/home/username
    sites
        DOMAIN1
            .env
            db.sqlite3
            manage.py etc
            static
            virtualenv
        DOMAIN2
            .env
            db.sqlite3
            etc
