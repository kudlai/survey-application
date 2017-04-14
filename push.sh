#!/bin/bash

version=1

docker tag ikudlay/survey-application ikudlay/survey-application:$version
docker push ikudlay/survey-application:$version
