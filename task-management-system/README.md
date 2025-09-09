# Task Management System
Bienvenidos al repositorio, aquí encontrareís mi entrega a la candidatura de Junior Python Developper.

Commandos útiles:
- docker ps
- docker run
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

## Para lanzarlo
```bash
git clone <repo>
cd task-management-system
cp .env.sample .env
docker-compose up
```
Visita la página en http://localhost:puerto
