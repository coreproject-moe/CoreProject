# Stage 1: Build stage
FROM python:3.12-alpine AS builder

# Install system dependencies
RUN apk add --no-cache \
    build-base \
    gcc \
    musl-dev \
    python3-dev

# Install uv
RUN pip install uv

# Set working directory
WORKDIR /app

# Copy only dependency files
COPY pyproject.toml uv.lock ./

# Create a virtual environment and install dependencies
RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    uv sync --frozen --no-dev

# Stage 2: Production stage
FROM python:3.12-alpine

# Install runtime dependencies
RUN apk add --no-cache libstdc++

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Set working directory
WORKDIR /app

# Copy application code
COPY . .

# Activate virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Set the command to run the application
CMD ["uv", "run", "coreproject_tracker"]