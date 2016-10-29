#!/bin/bash
./port_oldur.sh
python2 sunucu.py &
sleep 2
if which xdg-open > /dev/null
then
  xdg-open http://127.0.0.1:6060/
elif which gnome-open > /dev/null
then
 gnome-open http://127.0.0.1:6060/
fi
