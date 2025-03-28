# Stage 1: Builder
FROM python:3.13-alpine AS builder

ENV PATH="/root/.local/bin:$PATH"

# Install system dependencies
RUN apk update && apk add --no-cache curl gcc musl-dev

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Set working directory
WORKDIR /app

# Copy all files (including source code) into the container
COPY . .

# Remove any existing .venv directory
RUN rm -rf .venv

# Install dependencies and your package using the lockfile
RUN uv sync --no-cache-dir --no-default-groups 

# Stage 2: Final stage
FROM python:3.13-alpine

# Set working directory
WORKDIR /app

# Copy installed dependencies and source code from builder
COPY --from=builder /root/.local /root/.local
COPY --from=builder /usr/local /usr/local
COPY --from=builder /app /app

# Ensure the PATH is set correctly
ENV PATH="/app/.venv/bin:/root/.local/bin:/usr/local/bin:$PATH"

EXPOSE 5000/udp
EXPOSE 5000/tcp

# Run the app by directly invoking the module
# CMD ["sh", "-c", "while true; do sleep 30; done"] 
CMD [ "coreproject_tracker" ]