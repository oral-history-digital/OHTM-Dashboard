#!/bin/bash

# This is an example of how to run the Docker container.
docker run \
    --name ohtm-dashboard \
    --volume ~/ohtm/ohd.ohtm:/app/ohd.ohtm \
    --publish 8000:8000 \
    --detach \
    ohtm-dashboard:latest
