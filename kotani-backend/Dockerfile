# Stage 1: Builder
# Perbaiki warning casing: gunakan 'AS' huruf besar
FROM python:3.12-slim AS builder

WORKDIR /app

# Instal dependensi sistem yang dibutuhkan untuk kompilasi C
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    librdkafka-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Instal dependensi Python
RUN pip install --user --no-cache-dir -r requirements.txt

# ========================================== #

# Stage 2: Final
FROM python:3.12-slim AS final

WORKDIR /app

# Instal HANYA runtime library untuk Kafka (bukan -dev) agar image tetap ringan
RUN apt-get update && apt-get install -y --no-install-recommends \
    librdkafka1 \
    && rm -rf /var/lib/apt/lists/*

# Copy dependensi Python dari stage builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copy kode aplikasi backend Anda
COPY . .

# Pastikan port sesuai dengan app.py (contoh 8080)
EXPOSE 8080

# Jalankan aplikasi
CMD ["python", "app.py"]
