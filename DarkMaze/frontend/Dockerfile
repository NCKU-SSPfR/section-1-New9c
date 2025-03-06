# TODO: Install the frontend dependency package into the app folder inside the container.
FROM python:3.11
# Copy the backend requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8088", "--reload"]
