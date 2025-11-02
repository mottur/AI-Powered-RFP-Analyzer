# Server-side Dockerfile for Backend
FROM python:3.12

WORKDIR /app

# Copy only dependency files first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Expose the port the FastAPI app listens on
EXPOSE 5050

# Use a more production-ready command to run FastAPI with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5050"]