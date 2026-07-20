FROM python:3.9-slim

WORKDIR /app

# Install gettext for envsubst
RUN apt-get update && apt-get install -y gettext-base && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port
EXPOSE 80

# Run gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]
