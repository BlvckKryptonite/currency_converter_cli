# ---- Python builder stage ----
# I'm using a separate stage to install Python dependencies cleanly
FROM python:3.12-slim AS python-builder

WORKDIR /tmp
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt


# ---- Final stage ----
# I'm using the node:20-slim base since this is a Code Institute mock terminal app
# that wraps the Python CLI in a Node/xterm.js web interface
FROM node:20-slim
 
WORKDIR /app
 
# Install Python3, pip, and build tools needed for node-pty native compilation
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
 
# Copy and install Python dependencies directly — simpler and more reliable
# than copying from a builder stage across different Python versions
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt --break-system-packages
 
# Copy package.json first for better Docker layer caching
COPY package.json .
RUN npm install
 
# Copy the rest of the project
COPY . .
 
# Expose the port the Node server listens on
EXPOSE 8080
 
CMD ["node", "index.js"]