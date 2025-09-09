#!/bin/bash

# Esperar a que la base de datos esté lista usando herramientas de Django
# !! WARNING en --deploy, à seguir en produción.
# El operador ! invierte el resultado del comando:
# - Si manage.py check falla (exit code != 0), ! lo convierte en true, continúa el loop
# - Si manage.py check tiene éxito (exit code == 0), ! lo convierte en false, sale del loop
echo "Waiting for database to be ready..."
while ! python3 manage.py check --database default; do
    echo "Base de datos no disponible - esperando 2 segundos..."
    sleep 2
done
echo "✅ Base de datos lista!"

# Ejecuto las migraciones con manejo de errores
echo "Running migrations..."
if python3 manage.py makemigrations --noinput; then
    echo "✅ Migraciones creadas correctamente"
else
    echo "❌ Fallo al crear migraciones"
    exit 1
fi

if python3 manage.py migrate --noinput; then
    echo "✅ Migraciones aplicadas correctamente"
else
    echo "❌ Fallo al aplicar migraciones"
    exit 1
fi

# Creo el superuser con verificación
echo "Creating superuser..."
if python3 manage.py createsuperuser --noinput --username ${DJANGO_SUPERUSER_USERNAME} --email ${DJANGO_SUPERUSER_EMAIL}; then
    echo "✅ Superuser creado correctamente"
else
    echo "⚠️  Superuser ya existe o fallo al crearse"
fi

# Inicio el servidor
echo "🚀 Lanzando servidor Django en 0.0.0.0:${DJANGO_PORT}..."
python3 manage.py runserver 0.0.0.0:${DJANGO_PORT}