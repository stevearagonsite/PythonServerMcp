# Install uv
FROM python:3.12-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Change the working directory to the `app` directory
WORKDIR /app

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-editable

# Copy all files
COPY ./src ./src
COPY ./assets ./assets
COPY server.py ./server.py

# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    uv sync --frozen --no-editable

FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Set the time zone
ENV TZ=America/Argentina/Buenos_Aires
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install unix dependencies
RUN apt-get update && \
    apt-get install -y \
    # postgresql-client \
    git-lfs \
    ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Copy the environment and source code
COPY --from=builder --chown=app:app /app/.venv /app/.venv
COPY --from=builder --chown=app:app /app/src /app/src
COPY --from=builder --chown=app:app /app/server.py /app/server.py

# Create environment files if they don't exist
RUN touch /app/.env
RUN touch /app/.dev.env
RUN touch /app/.staging.env
RUN touch /app/.prod.env

# Copy start script
COPY start.sh ./start.sh
RUN chmod +x ./start.sh

# Run start script
ENTRYPOINT ["./start.sh"]
