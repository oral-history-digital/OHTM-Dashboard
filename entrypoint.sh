#!/bin/bash
set -e

if [ -z "$OHTM_FILE" ]; then
  echo >&2 '[ERROR]: specify OHTM_FILE env var'
  exit 1
fi

exec "$@" # run the default command
