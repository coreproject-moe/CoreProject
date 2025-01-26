# Pyloid-SvelteKit

Pyloid-SvelteKit-boilerplate is a template for projects combining a SvelteKit frontend with a Python backend. Here, we'll explain in detail the project setup, development, and build process.

### Prerequisites

- [Prerequisites](https://docs.pyloid.com/getting-started/prerequisites)

## 1. Project Initialization

Before starting the project, you need to install all necessary dependencies.

```bash
npm install # node
poetry install # python
```

These commands performs the following tasks:

1. Install npm packages
2. Create a Python virtual environment using poetry (.venv)
3. Install Python dependencies (based on pyproject.toml)

## 2. Running the Development Server

During development, you can run both frontend and backend servers simultaneously with the following command:

```bash
npm run dev # sveltekit
poetry run poe dev # pyloid
```

These commands performs the following tasks:

1. Run the SvelteKit frontend development server using Vite
2. Run the Python backend server (run.py)

The concurrently package is used to run both processes in parallel.

## 3. Building the Project

To build the project for production deployment, use the following command:

```bash
npm run build # sveltekit
poetry run poe build # pyloid
```

These commands performs the following tasks:

1. Frontend build using Vite
2. Package the Python backend into an executable using PyInstaller

### How PyInstaller Works

1. Dependency Analysis: PyInstaller analyzes the Python script and its dependencies.
2. File Collection: It collects all necessary Python modules, libraries, and data files.
3. Binary Generation: It packages the collected files into a single directory or a single executable file.

### Important Notes

- Cross-platform Builds: You need to perform the build for each platform on the respective operating system.
- Environment Variables: You may need to set environment variables appropriately depending on the production environment.

This guide should help you understand the process of initializing, developing, and building a project using the Pylon Boilerplate. Backend packaging with PyInstaller simplifies deployment and facilitates dependency management.
