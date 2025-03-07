FROM python:3.11

# Create a non-root user
RUN useradd -m nonrooter 

WORKDIR /backend

# Copy the backend requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files

COPY src/ ./src/

# Change ownership to the non-root user
RUN chown -R nonrooter:nonrooter /backend
# Switch to non-root user
USER nonrooter

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000",  "--reload"]
