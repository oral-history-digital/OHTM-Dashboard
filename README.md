# Oral History Topic Modeling Dashboard

## Requirements

- Python 3.13

## Installation

### With pip

Create and activate an environment and install the requirements.

```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### With uv

```shell
uv sync
```

## Usage

Copy the main_template.py file to main.py and adjust your file settings.
Then run main.py

```shell
python main.py
```

or

```shell
uv run main.py
```

## Usage with Docker

A public Docker image is built with every push to the master branch.

Start the Docker container by running

```shell
./run-docker.sh
```

First adapt the volume option (the first part before the colon) so
that it points to an ohtm file on your computer.

With the container running, the dashboard should be available at
http://localhost:8000
