# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# [Option] Install Docker
RUN curl -fsSL https://get.docker.com -o get-docker.sh \
    && apt-get install -y wget \
    && sh get-docker.sh \
    && usermod -aG docker root \
    && apt autoremove

RUN apt autoremove \
    && pipx install --system-site-packages --pip-args=--no-cache-dir --pip-args=--force-reinstall pytest \