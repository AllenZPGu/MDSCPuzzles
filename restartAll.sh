#!/bin/bash
. /home/allen/MDSCPuzzles/mdscenv/bin/activate
python /home/allen/MDSCPuzzles/MDSCProj/manage.py collectstatic
echo Collected static
sudo systemctl restart gunicorn.socket gunicorn.service
echo Restarted gunicorn.socket, gunicorn.service
sudo systemctl restart gunicorn
echo Restarted gunicorn
sudo systemctl restart nginx
echo Restarted nginx
