# Usamos una imagen de Python ligera (Debian Bookworm slim)
FROM python:3.12-slim-bookworm

# Evitar que Python genere archivos .pyc y asegurar salida de logs limpia
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Instalamos dependencias del sistema para que lxml y pandas funcionen
RUN apt-get update && apt-get install -y \
    gcc \
    libxml2-dev \
    libxslt-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiamos el requirements.txt desde la raíz al contenedor
COPY requirements.txt .

# Instalamos las librerías de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el proyecto al contenedor
COPY . .

# Mantenemos el contenedor encendido para que no se muera al terminar
CMD ["tail", "-f", "/dev/null"]
