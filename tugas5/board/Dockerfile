# Gunakan Python resmi
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt dan install dependency
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua file project ke dalam container
COPY . .

# Expose port Flask
EXPOSE 5000

# Jalankan aplikasi Flask
CMD ["python", "app.py"]
