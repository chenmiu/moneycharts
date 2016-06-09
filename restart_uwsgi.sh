#!/bin/bash

NAME=uwsgi_moneycharts
set -x
pkill $NAME
sleep 1
uwsgi_python -x django_uwsgi.xml --enable-threads --post-buffering 1 --procname $NAME

