FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script
COPY check_ip.py /app/

# Command to run the script
CMD ["python", "check_ip.py"]
