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

# Install Python3 and curl from Debian's default repos
# Note: python3.12 is not available via apt on Bookworm — python3 (3.11) is used instead
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy installed Python packages from builder stage
COPY --from=python-builder /root/.local /root/.local

# Make sure Python user packages are on the PATH
ENV PATH=/root/.local/bin:$PATH \
    PYTHONPATH=/root/.local/lib/python3.11/site-packages

# Copy package.json first for better Docker layer caching
COPY package.json .
RUN npm install

# Copy the rest of the project
COPY . .

# Expose the port the Node server listens on
EXPOSE 8000

# Start the Node server which runs the mock terminal
CMD ["node", "index.js"]