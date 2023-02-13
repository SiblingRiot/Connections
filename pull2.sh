#!/bin/bash

function pull {
 git pull
 password
 service nginx reload
}

pull;


