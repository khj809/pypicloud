FROM python:3.8-alpine3.12
MAINTAINER Steven Arcangeli <stevearc@stevearc.com>

EXPOSE 8080
WORKDIR /app/

# Install packages required
ENV PYPICLOUD_VERSION 1.3.12
ENV CARGO_NET_GIT_FETCH_WITH_CLI true
ADD pyproject.toml setup.py README.rst CHANGES.rst MANIFEST.in requirements_test.txt ./pypicloud/
ADD pypicloud ./pypicloud/pypicloud
RUN --mount=type=tmpfs,target=/root/.cargo \
  apk add --no-cache --virtual build-deps python3-dev mariadb-dev postgresql-dev build-base gcc \
  linux-headers openldap-dev autoconf automake make libffi-dev libressl-dev musl-dev git curl \
  mariadb-connector-c-dev util-linux-dev g++ \
  && curl –proto '=https' –tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
  && source ~/.cargo/env \
  && apk add --no-cache libldap libpq mariadb-connector-c libgcc \
  && cd ./pypicloud \
  && python -m pip install --no-cache-dir --upgrade pip \
  && python -m pip install --no-cache-dir .[all_plugins] \
    requests uwsgi pastescript mysqlclient psycopg2-binary bcrypt cryptography \
    --no-binary cryptography,uwsgi \
  && cd .. \
  && rm -rf ./pypicloud \
  && adduser -D -s /bin/sh -h /var/lib/pypicloud/ pypicloud \
  && apk del --no-cache build-deps \
  && mkdir -p /etc/pypicloud

# Add the command for easily creating config files
ADD ./docker/py3-alpine/config.ini /etc/pypicloud/config.ini
ADD ./docker/py3-alpine/make-config.sh /usr/local/bin/make-config

# Create a working directory for pypicloud
VOLUME /var/lib/pypicloud

# Run as pypicloud user
USER pypicloud

CMD ["uwsgi", "--die-on-term", "/etc/pypicloud/config.ini"]
