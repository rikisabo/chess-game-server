# Chess Game Server - Railway Docker
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all necessary files
COPY server/ ./server/
COPY shared/ ./shared/
COPY pieces/ ./pieces/

# Expose port
EXPOSE 8000

# Start the server
CMD ["python", "server/main.py"]
