# Stage 1: Builder
FROM python:3.12-slim as builder
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final
FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH=/root/.local/bin:$PATH \
    APP_TMP_DATA=/tmp

WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .

# Praktik Keamanan: Jangan jalankan container sebagai root
RUN useradd -m -d /home/kotaniuser -s /bin/bash kotaniuser \
    && chown -R kotaniuser:kotaniuser /app \
    && chmod -R g=u /app

USER kotaniuser
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=5s CMD curl --fail http://localhost:8080/health || exit 1

CMD ["python", "app.py"]
