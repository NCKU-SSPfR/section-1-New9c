# TODO: Install the backend dependency package into the app folder inside the container.

FROM python:3.11

WORKDIR /backend
# Copy the backend requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000",  "--reload"]
