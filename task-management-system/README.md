# Task Management System
Bienvenidos al repositorio, aquí encontrareís mi entrega a la candidatura de Junior Python Developper.

## Para lanzarlo
```bash
git clone <repo>
cd task-management-system
cp .env.sample .env
docker-compose up
```
Visita la página en http://localhost:7777

Commandos útiles:
- docker ps
- docker run
- docker logs
- docker-compose build [container]
- docker-compose volume ls/rm
- docker-compose network ls/rm
- docker-compose exec [container] [command]
- docker-compose up

He escogido una imagen de postgres versión 15. El enunciado no menciona un Dockerfile para otro servicio dedicado a la base de datos. Implica que no nos hace falta predefinir usuarios roles y tablas ya que django lo hace muy bien con sus Migraciones.

El proyecto de Django se encuentra en django_backend:
- config/ -> principal archivos de configuración de Django
- api/ -> aplicación restframework con endpoints sobre los modelos.
- entrypoint.sh -> script de inicio, configura contenedor Django.

Desafortunadamente no he tenido tiempo de desplegar Redis y Celery.

**Endpoints REST desplegados:**
**Auth por Session**
### POST /api/auth/register/
### POST /api/auth/login/
### POST /api/auth/logout/
### POST /api/auth/refresh/
**User Management:**
### GET /api/users/ (list with pagination)
### GET /api/users/{id}/
### PUT /api/users/{id}/
### GET /api/users/me/

**View /**
### GET / -> template simplisssimo

**Panel admin**
### GET /admin/


