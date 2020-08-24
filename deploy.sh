#!/usr/bin/env bash
docker build . -t swampman:latest
sudo docker run -d swampman:latest
