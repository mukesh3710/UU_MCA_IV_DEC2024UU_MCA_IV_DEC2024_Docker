# Use minimal RHEL8 base image
FROM registry.access.redhat.com/ubi8/ubi-minimal

# Set environment variables for non-interactive installs
ENV LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    PYTHON_VERSION=3.8.5

# Install necessary packages and Python
RUN microdnf update -y && \
    microdnf install -y gcc gcc-c++ make \
                       libffi-devel \
                       openssl-devel \
                       bzip2 \
                       bzip2-libs \
                       bzip2-devel \
                       wget \
                       tar \
                       gzip && \
    wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz && \
    tar xzf Python-$PYTHON_VERSION.tgz && \
    cd Python-$PYTHON_VERSION && \
    ./configure --enable-optimizations && \
    make altinstall && \
    cd .. && \
    rm -rf Python-$PYTHON_VERSION Python-$PYTHON_VERSION.tgz && \
    microdnf clean all

# Add requirements file and install dependencies
WORKDIR /app
COPY app/ /app/
RUN python3.8 -m pip install --upgrade pip && \
    python3.8 -m pip install -r requirements.txt

# Expose default app port
EXPOSE 9000

# Set the default command to Python
CMD ["python3.8", "app.py"]
