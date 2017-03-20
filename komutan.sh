#!/bin/bash
./port_oldur.sh
sudo gunicorn -w 2 -b 127.0.0.1:6060 sunucu:app -t 240 &
sleep 2
if which xdg-open > /dev/null
then
  xdg-open http://127.0.0.1:6060/
elif which gnome-open > /dev/null
then
 gnome-open http://127.0.0.1:6060/
fi
