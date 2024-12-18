# UU_MCA_IV_DEC2024UU_MCA_IV_DEC2024_Docker

# Python 3.8 Application on RHEL8 Minimal Docker Image

This repository provides a Dockerfile to build and run a Python 3.8 application on a minimal Red Hat Universal Base Image (UBI8). The Dockerfile installs necessary dependencies, sets up the application environment, and exposes a default port (9000) for the application.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Dockerfile Breakdown](#dockerfile-breakdown)
- [Building the Docker Image](#building-the-docker-image)
- [Running the Container](#running-the-container)
- [Exposing the Application Port](#exposing-the-application-port)
- [Notes](#notes)

---

## Prerequisites

Before using this Dockerfile, you need:

- [Docker](https://www.docker.com/get-started) installed on your machine or server.
- A `requirements.txt` file in your project directory with all the Python dependencies. (find it under app/ direcotry)
- Your Python application (`app.py`) and any other related files in the `app/` directory.

---

## Dockerfile Breakdown

This Dockerfile does the following:

1. **Base Image**: Uses the `ubi8/ubi-minimal` image as the foundation for the container.
2. **Environment Variables**: Sets up environment variables for locale and Python version.
3. **Install Dependencies**: Installs system packages required for building Python from source, as well as Python 3.8.5.
4. **Copy Application Files**: Copies your application code into the container.
5. **Install Python Dependencies**: Installs Python dependencies listed in the `requirements.txt` file.
6. **Expose Port**: Exposes port `9000` for communication with the application.
7. **Set Default Command**: Runs the Python application (`app.py`) when the container starts.

---

## Building the Docker Image

To build the Docker image, run the following command in the root directory of your project (where the `Dockerfile` is located):

```bash
docker build -t python-app .
```

---

## Exposing the Application Port

The application is configured to listen on port 9000 by default. To expose this port on your host machine, you should map the container's internal port 9000 to a port on your host when running the container:

```bash
docker run -d -p 9000:9000 python-app
```

You can access your application by navigating to http://localhost:9000 (or the host’s IP address) in your browser or via an HTTP request.

---

## Notes

Ensure that your Python application (app.py) is the entry point, and it is located in the /app directory inside the container.
The requirements.txt file should include all the necessary Python packages your application needs.
The default port exposed is 9000. You can modify the EXPOSE directive and the port mapping (-p) if your application uses a different port.
If you need to customize the Python version, update the PYTHON_VERSION environment variable in the Dockerfile.
