# Gunakan Python sebagai base image
FROM python:3.12-slim

# Set working directory di dalam container
WORKDIR /app

# Salin file requirements.txt
COPY requirements.txt .

# Instal semua dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file proyek ke dalam container
COPY . .

# Atur variabel environment untuk Django
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE main.settings

# Jalankan aplikasi Django menggunakan server bawaan
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
