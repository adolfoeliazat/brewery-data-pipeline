# Use official Python image as a base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the code into the container
COPY . .

# Set up environment variables (adjust these as needed)
ENV AWS_REGION="us-east-1"
ENV S3_BUCKET_NAME="ecommerce-sales-data-bucket"

# Run the main pipeline script
CMD ["python", "main_pipeline.py"]
