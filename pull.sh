#!/bin/bash

cd /home/pi/MagicMirror/Connections

function pull {
 git pull
 password
 service nginx reload
}


pull;

