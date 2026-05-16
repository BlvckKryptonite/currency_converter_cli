# Stage 1: Build Python dependencies
FROM python:3.12-slim as python-builder

WORKDIR /tmp

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Runtime image with Node.js
FROM node:20-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.12 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy Python packages from builder stage
COPY --from=python-builder /root/.local /root/.local

# Copy Node.js dependencies
COPY package.json ./
RUN npm install --production

# Copy application code
COPY . .

# Set environment variables
ENV PATH=/root/.local/bin:$PATH
ENV PORT=8080
ENV NODE_ENV=production
ENV PYTHONUNBUFFERED=1

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:${PORT}/ || exit 1

# Run the Node.js web server (which serves the terminal interface)
CMD ["node", "index.js"]
