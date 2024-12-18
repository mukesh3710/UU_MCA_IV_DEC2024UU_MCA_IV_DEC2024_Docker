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
- A `requirements.txt` file in your project directory with all the Python dependencies.
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
