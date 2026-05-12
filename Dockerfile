# Base image Python 3.9
FROM python:3.9-slim

WORKDIR /app

# Pehle requirements copy karein aur install karein
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Phir baaki saara code copy karein
COPY . .

# Flask ki settings
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Port 5000 expose karein
EXPOSE 5000

# Container chalne par ye command run hogi
CMD ["flask", "run"]