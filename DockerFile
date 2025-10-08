# Base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY calculator/ ./calculator/
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the calculator when container starts
CMD ["python3", "calculator/calculator.py"]
