# Task Management System
Bienvenidos al repositorio, aquí encontrareís mi entrega a la candidatura de Junior Python Developper.

Commandos útiles:
- docker-compose build [container]
- docker-compose volume ls
- docker-compose network ls
- docker-compose exec [container] [command]

He escogido una imagen de postgres versión 15. El enunciado no menciona un Dockerfile para otro servicio dedicado a la base de datos. Implica que no nos hace falta predefinir usuarios roles y tablas ya que django ORM lo hace muy bien.
## Quick Start
```bash
git clone <repo>
cd task-management-system
cp .env.sample .env
docker-compose up