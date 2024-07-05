#!/bin/bash

app="docker.insidecode"
docker build -t ${app} .
docker run -d -p 80:80 -v insidecode:/var/www/app/docs ${app}
