# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy dependencies & install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app code
COPY . .

# Run app
CMD ["python", "app.py"]


# https://chatgpt.com/c/68b9b609-2770-8329-b92d-8dd4fedd2390 -- open in chrome to continue