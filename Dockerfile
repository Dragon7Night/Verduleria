# ============================================================
# FROM: Imagen base de Python 3.13 en versión ligera (slim)
# - Usamos 'slim' basada en Debian para mantener la imagen
#   pequeña pero con total compatibilidad para librerías de Python.
# ============================================================
FROM python:3.13-slim

# ============================================================
# ENV: Variables de entorno recomendadas para contenedores Python
# - PYTHONDONTWRITEBYTECODE=1: Evita que Python genere archivos .pyc
#   innecesarios dentro del contenedor.
# - PYTHONUNBUFFERED=1: Asegura que los logs de Django aparezcan
#   al instante en la consola de Docker sin retrasos.
# ============================================================
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ============================================================
# WORKDIR: Define el directorio de trabajo principal dentro
# del contenedor. Todos los comandos subsiguientes se ejecutarán aquí.
# ============================================================
WORKDIR /app

# ============================================================
# RUN: Instala dependencias del sistema operativo necesarias
# para compilar ciertas librerías de Python si lo requiere el proyecto.
# ============================================================
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# ============================================================
# COPY & PIP: Copiamos primero el requirements.txt e instalamos
# las dependencias. Esto aprovecha la caché de Docker: si no cambias
# las librerías, este paso no se vuelve a descargar al reconstruir.
# ============================================================
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# ============================================================
# COPY: Copia el resto del código fuente de tu proyecto 
# (Apps, Verduleria, static, templates, manage.py, etc.) 
# al directorio de trabajo del contenedor (/app).
# ============================================================
COPY . /app/

# ============================================================
# EXPOSE: Documenta el puerto en el que correrá Django
# (por defecto Django usa el puerto 8000).
# ============================================================
EXPOSE 8000

# ============================================================
# CMD: El comando que se ejecutará automáticamente cuando
# el contenedor arranque. 
# - '0.0.0.0:8000' es vital para que Django acepte conexiones
#   externas desde otros contenedores o desde tu propia máquina.
# ============================================================
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]