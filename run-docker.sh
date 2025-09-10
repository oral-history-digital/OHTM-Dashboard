#!/bin/bash

# This is an example of how to run the Docker container.
docker run \
    --name dashboard \
    --volume ~/ohtm/ohd.ohtm:/app/ohd.ohtm \
    --env OHTM_FILE=/app/ohd.ohtm \
    --publish 8000:8000 \
    --detach \
    ohtm:latest
