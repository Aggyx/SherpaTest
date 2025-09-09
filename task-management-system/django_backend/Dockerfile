# Builder stage, cuando se construye la imagen
FROM python:3.11-slim AS builder

# Actualizar y limpiar la lista de paquetes
RUN apt-get update && rm -rf /var/lib/apt/lists/*

# Crear y activar el entorno virtual
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copiar los requirements y instalar las dependencias de Python
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Runtime stage, justo antes de ejecutar la imagen
FROM python:3.11-slim AS runtime

# Instalar cliente PostgreSQL
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Creo un usuario no root para seguridad ya que en la imagen base es root
RUN groupadd -r django && useradd -r -g django django

# Copiar el entorno virtual desde el stage de builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /django_backend

COPY . .

RUN chown -R django:django /django_backend && \
    chmod -R 755 /django_backend

USER django
# Expose port (uncomment when ready to run server)
# EXPOSE 8000

CMD ["/bin/bash", "entrypoint.sh"]