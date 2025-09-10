# syntax=docker/dockerfile:1

# Separate build image #################################################
FROM python:3.13.7-slim-trixie AS build

SHELL ["sh", "-exc"]

# Install and configure uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON=python3.13 \
    UV_PROJECT_ENVIRONMENT=/app

# Synchronize DEPENDENCIES without the application itself.
RUN --mount=type=cache,target=/root/.cache \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync \
    --locked \
    --no-dev \
    --group prod \
    --no-install-project

########################################################################


FROM python:3.13.7-slim-trixie

ARG VERSION="0.1.0"

LABEL org.opencontainers.image.title="OHTM Dashboard"
LABEL org.opencontainers.image.description="OHTM Dashboard"
LABEL org.opencontainers.image.ref.name="ohtm-dashboard:latest"
LABEL org.opencontainers.image.version="${VERSION}"
LABEL org.opencontainers.image.authors="Philipp Bayerschmidt <philipp.bayerschmidt@fernuni-hagen.de>,Marc Altmann <m.altmann@fu-berlin.de>"
LABEL org.opencontainers.image.source="https://github.com/oral-history-digital/OHTM-Dashboard"

SHELL ["sh", "-exc"]

ENV APPROOT="/app"
ENV PATH=/app/bin:$PATH
ENV OHTM_FILE=/app/ohd.ohtm

VOLUME /app/ohd.ohtm

RUN <<EOT
groupadd -r app
useradd -r -d /app -g app -N app
EOT

STOPSIGNAL SIGINT

RUN <<EOT
apt-get update -qy
apt-get install -qyy \
    -o APT::Install-Recommends=false \
    -o APT::Install-Suggests=false \
    netcat-traditional \
    vim
apt-get clean
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
EOT

# Copy dependencies from build image
COPY --from=build --chown=app:app /app /app

# Copy app itself
COPY --chown=app:app . /app

COPY ["./entrypoint.sh", "/"]
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD nc -vz -w 2 localhost 8000

USER app
WORKDIR ${APPROOT}

CMD ["gunicorn", "ohtm_dash_server:server", "--bind", "0.0.0.0"]
