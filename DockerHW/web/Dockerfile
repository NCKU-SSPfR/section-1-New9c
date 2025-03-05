FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /web

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Set the command to run the application
CMD ["python", "main.py"]
