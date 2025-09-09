# Arquitectura del Sistema - Sistema de Gestión de Tareas

## Visión General

El sistema de gestión de tareas está diseñado como una aplicación web basada en microservicios utilizando Docker para el despliegue y orquestación. La arquitectura actual se centra en un backend Django con base de datos PostgreSQL, preparada para futuras expansiones con servicios adicionales.

## Arquitectura de Alto Nivel

```
┌─────────────────────────────────────────────────────────────┐
│                    Cliente Web/Frontend                     │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTP/HTTPS
┌─────────────────────▼───────────────────────────────────────┐
│                Docker Network                               │
│  ┌─────────────────┐    ┌─────────────────────────────────┐ │
│  │   Django API    │    │      PostgreSQL Database        │ │
│  │   (Backend)     │◄──►│      (Data Storage)             │ │
│  │   Port: 8000    │    │      Port: 5432                 │ │
│  └─────────────────┘    └─────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## Componentes del Sistema

### 1. Backend Django (API REST)

**Tecnologías:**
- Django 5.2.6
- Django REST Framework
- Python 3.x

**Características:**
- API REST con autenticación basada en sesiones
- Serializers personalizados para validación de datos
- Vistas basadas en clases genéricas (GenericAPIView)
- Configuración para desarrollo y producción

**Estructura de la aplicación:**
```
django_backend/
├── api/                   # Aplicación principal
│   ├── models.py          # Modelos de datos
│   ├── admin.py           # Configuración del admin
│   ├── urls.py            # Rutas de la API
│   ├── serializers/       # Serializers por módulo
│   │   ├── auth/          # Autenticación
│   │   ├── users/         # Gestión de usuarios
│   │   └── tasks/         # Gestión de tareas (pendiente)
│   └── views/             # Vistas por módulo
│       ├── auth/          # Endpoints de autenticación
│       ├── users/         # Endpoints de usuarios
│       └── tasks/         # Endpoints de tareas (pendiente)
├── config/                # Configuración de Django
│   ├── settings.py        # Configuración principal
│   ├── urls.py           # URLs principales
│   └── wsgi.py           # WSGI para producción
├── Dockerfile            # Imagen Docker
├── requirements.txt      # Dependencias Python
└── manage.py            # Script de gestión Django
```

### 2. Base de Datos PostgreSQL

**Configuración:**
- PostgreSQL 15 (Debian Bookworm)
- Puerto: 5432
- Almacenamiento: Volumen Docker nombrado
- Configuración optimizada para desarrollo

**Modelos de Datos:**

#### Usuario (User)
- Modelo estándar de Django
- Campos: username, password, email, first_name, last_name
- Autenticación integrada

#### Tarea (Task)
- **Relaciones:**
  - `created_by`: ForeignKey a User (creador)
  - `assigned_ToUsers`: ManyToMany a User (asignados)
  - `tags`: ManyToMany a Tag (etiquetas)
  - `parent_task`: ForeignKey a Task (tarea padre)
- **Campos principales:**
  - `title`, `description`: Información básica
  - `status`: Estado (todo, in_progress, done)
  - `priority`: Prioridad (low, medium, high)
  - `due_date`: Fecha de vencimiento
  - `estimated_hours`, `actual_hours`: Control de tiempo
  - `metadata`: JSON para datos adicionales
  - `is_archived`: Control de archivado

#### Etiqueta (Tag)
- Relación ManyToMany con Task
- Campos: name, timestamps

### 3. Contenedorización con Docker

**Docker Compose:**
```yaml
services:
  web:
    build: ./django_backend
    ports: ["8000:8000"]
    volumes: [bind-mount para desarrollo]
    depends_on: [database_postgres]
    networks: [task_management_network]
  
  database_postgres:
    image: postgres:15
    environment: [variables de entorno]
    volumes: [named-volume para persistencia]
    networks: [task_management_network]
```

**Estrategia de Volúmenes:**
- **Desarrollo:** Bind-mount para Django (código en tiempo real)
- **Desarrollo:** Named-volume para PostgreSQL (persistencia de datos)
- **Producción:** Named-volumes para ambos servicios

### 4. Redes Docker

**Configuración:**
- Red personalizada: `task_management_network`
- Resolución DNS automática entre contenedores
- Aislamiento de la red host

## Patron de Diseño Implementado

### Patrón MVC (Model-View-Controller)
- **Modelos:** Definición de datos en `models.py`
- **Vistas:** Lógica de negocio en `views/`
- **Controladores:** Serializers para validación y transformación

## Flujo de Datos

### Autenticación
```
Cliente → POST /api/auth/login/ → LoginSerializer → authenticate() → Session → Response
```

### Gestión de Usuarios
```
Cliente → API Endpoint → View → Serializer → Model → Database → Response
```

### Flujo de una Petición Típica
1. **Cliente** envía petición HTTP
2. **Django** procesa la URL y middleware
3. **View** ejecuta lógica
4. **Serializer** valida y transforma datos
5. **Model** interactúa con la base de datos
6. **Response** devuelve datos serializados

## Configuración de Seguridad

### Autenticación
- **Método:** Sesiones de Django
- **Duración:** 24 horas
- **Almacenamiento:** Base de datos
- **Seguridad:** HTTPOnly cookies

### Validación de Contraseñas
- Mínimo 8 caracteres
- Validadores estándar de Django
- Hash seguro con PBKDF2

### Configuración de Producción (pendiente)
- HTTPS obligatorio
- SECRET_KEY seguro
- DEBUG = False
- ALLOWED_HOSTS restringido
- SESSION_COOKIE_SECURE = True

### Estrategia de Escalabilidad

#### Horizontal
- Múltiples instancias de Django con load balancer
- Replicación de base de datos
- Servicios independientes escalables

#### Vertical
- Optimización de consultas de base de datos
- Caching con Redis (futuro)
- CDN para archivos estáticos


## Monitoreo y Logging
### Logs de Aplicación
- Logs de Django en stdout


## Consideraciones de Producción

### Despliegue
- (molaría) CI/CD pipeline con guihub para despliegue automático
- Health checks para servicios

### Backup y Recuperación
- Backups automáticos de PostgreSQL
- Estrategia de recuperación ante desastres
- Replicación de datos críticos

### Rendimiento
- Configuración de conexiones de base de datos
- Caching de consultas frecuentes
- Optimización de índices de base de datos

## Decisiones Arquitectónicas

### 1. Elección de PostgreSQL
- **Razón:** Soporte nativo para JSON, relaciones complejas
- **Alternativas consideradas:** MySQL, SQLite
- **Justificación:** Escalabilidad y características avanzadas

### 2. Autenticación por Sesiones
- **Razón:** Simplicidad para aplicaciones web tradicionales
- **Alternativas consideradas:** JWT, OAuth2
- **Justificación:** Integración nativa con Django, seguridad robusta

### 3. Docker para Desarrollo
- **Razón:** Consistencia entre entornos
- **Justificación:** Facilita despliegue y colaboración

### 4. Estructura Modular de Serializers
- **Razón:** Mantenibilidad y organización
- **Justificación:** Escalabilidad y separación de responsabilidades
