FROM node:20-slim

WORKDIR /app

# Install Python for the CLI app
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.12 \
    python3-pip \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy Node.js dependencies
COPY package.json ./
RUN npm install --production

# Copy Python requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV PORT=8080
ENV NODE_ENV=production
ENV PYTHONUNBUFFERED=1

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:${PORT}/ || exit 1

# Run the Node.js web server (which serves the terminal interface)
CMD ["node", "index.js"]
