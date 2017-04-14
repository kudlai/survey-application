#!/bin/bash

docker rm -f pytest 
docker create -p 8000:8000 --name pytest pytest
docker start pytest

