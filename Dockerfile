# Use a lightweight Python 3.7 base image
FROM python:3.7-slim-buster

# Set the working directory inside the container
WORKDIR /app


# Copy only requirements first to leverage Docker caching
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /app


# Default command to run the application
CMD ["python3", "app.py"]
