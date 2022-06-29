#!/bin/bash
. /home/allen/MDSCPuzzles/mdscenv/bin/activate
python /home/allen/MDSCPuzzles/MDSCProj/manage.py runscript getGuesses --script-args $1 $2
