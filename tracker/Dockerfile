FROM python:3.13-alpine AS builder

ENV PATH="/root/.local/bin:$PATH"

# Install system dependencies
RUN apk update && apk add --no-cache curl gcc musl-dev

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Set working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies using the lockfile
RUN uv pip install --system .

# Stage 2: Final stage
FROM python:3.13-alpine

# Set working directory
WORKDIR /app

# Copy only installed dependencies from builder
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application source code
COPY . .

EXPOSE 8001/udp
EXPOSE 9000/tcp
EXPOSE 12000/tcp

# Set the default command
CMD ["python", "src/run.py"]