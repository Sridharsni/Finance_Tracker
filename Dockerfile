# Use official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt into the container at /app
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app will run on
EXPOSE 5000

# Set the environment variable to make Flask output directly to console
ENV FLASK_ENV=development

# Run the Flask app
CMD ["python", "app.py"]

