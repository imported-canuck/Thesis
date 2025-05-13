# .devcontainer/Dockerfile
# --------------------------------------------------------------------
# 1) Start from an official CPython 3.6 image
FROM python:3.6.8-slim-buster                    

# 2) Codespace tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends git curl build-essential && \
    rm -rf /var/lib/apt/lists/*

# 3) Copy requirements and pre-install them
COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install --upgrade pip \
 && python -m pip install -r /tmp/requirements.txt

# 4) Default workdir matches Codespace mount point
WORKDIR /workspaces/${GITHUB_REPOSITORY##*/}
