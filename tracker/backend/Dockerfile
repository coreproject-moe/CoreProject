# Stage 1: Builder
FROM python:3.13-alpine AS builder

ENV PATH="/root/.local/bin:$PATH"

# Install system dependencies
RUN apk update && apk add --no-cache curl gcc musl-dev

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Remove any existing .venv directory
RUN rm -rf .venv

# Install dependencies
RUN uv sync --no-cache-dir --no-default-groups

# Stage 2: Final stage
FROM python:3.13-alpine

# Set default environment variables
ENV HOST=127.0.0.1
ENV PORT=5000

WORKDIR /app

# Copy installed dependencies and source code
COPY --from=builder /root/.local /root/.local
COPY --from=builder /usr/local /usr/local
COPY --from=builder /app /app

# Ensure the PATH is set correctly
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 5000/udp 5000/tcp

# Use shell form to allow environment variable substitution
CMD ["sh", "-c", "coreproject_tracker --host ${HOST} --port ${PORT}"]