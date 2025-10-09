# Base image
FROM python:3.13-slim

# Set working directory
# WORKDIR /app

# Copy project file
COPY calculator/ ./calculator/
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# back to normal.
CMD ["python3", "calculator/calculator.py"]
