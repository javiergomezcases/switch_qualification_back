#!/usr/bin/env bash

FILE_DIR="$(dirname $0)"
cd $FILE_DIR
export DJANGO_READ_DOT_ENV_FILE=True

docker-compose up -d