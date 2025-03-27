# Skip virtual environment and use system Python
FROM python:3.12-slim-bookworm

RUN pip install uv
WORKDIR /app
COPY pyproject.toml uv.lock ./

# Install directly to system Python
RUN uv sync --frozen

COPY . .
CMD ["uv", "run", "coreproject_tracker"]