#!/bin/bash

# This is an example of how to run the Docker container.
docker run \
  --name dashboard \
  -v ~/ohtm/ohd.ohtm:/app/ohd.ohtm \
  -e OHTM_FILE=/app/ohd.ohtm \
  -p 8000:8000 \
  -d \
  ohtm:latest
