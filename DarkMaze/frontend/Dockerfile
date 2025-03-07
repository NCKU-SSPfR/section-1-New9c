FROM python:3.11

# Create a non-root user
RUN useradd -m nonroot 

WORKDIR /frontend

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

# Switch to non-root user
USER nonroot

# Run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8088", "--reload"]
