# Documentación de la API - Sistema de Gestión de Tareas

## Información General

Esta API REST está construida con Django y Django REST Framework para gestionar un sistema de tareas con autenticación de usuarios. La API utiliza autenticación basada en sesiones y está diseñada para ser consumida por aplicaciones web.

**Base URL:** `http://localhost:{DJANGO_PORT}/api/`

## Autenticación

La API utiliza autenticación basada en sesiones de Django. Los usuarios deben autenticarse para acceder a la mayoría de los endpoints, excepto el registro y login.

## Endpoints de Autenticación

### POST /api/auth/register/
**Descripción:** Registra un nuevo usuario en el sistema.

**Permisos:** Público (AllowAny)

**Cuerpo de la petición:**
```json
{
    "username": "usuario123",
    "password": "contraseña123"
}
```

**Respuesta exitosa (201):**
```json
{
    "username": "usuario123"
}
```

**Características:**
- Crea un nuevo usuario con contraseña hasheada
- Valida que la contraseña tenga al menos 8 caracteres
- Utiliza el modelo User estándar de Django
- Implementado con `CreateAPIView`


### POST /api/auth/login/
**Descripción:** Autentica un usuario existente y crea una sesión.

**Permisos:** Público (AllowAny)

**Cuerpo de la petición:**
```json
{
    "username": "usuario123",
    "password": "contraseña123"
}
```

**Respuesta exitosa (200):**
```json
{
    "mensaje": "Login exitoso",
    "usuario": {
        "username": "usuario123"
    }
}
```

**Respuesta de error (400):**
```json
{
    "non_field_errors": ["Invalid credentials"]
}
```

**Características:**
- Valida credenciales usando `authenticate()` de Django
- Verifica que el usuario esté activo
- Crea una sesión de usuario
- Implementado como función con decoradores `@api_view`

### POST /api/auth/logout/
**Descripción:** Cierra la sesión del usuario autenticado.

**Permisos:** Requiere autenticación (IsAuthenticated)

**Respuesta exitosa (200):**
```json
{
    "mensaje": "Logout exitoso"
}
```

**Características:**
- Cierra la sesión actual del usuario
- Implementado como función con decoradores `@api_view`

### GET /api/auth/refresh/
**Descripción:** Refresca la sesión y devuelve los datos del usuario actual.

**Permisos:** Requiere autenticación (IsAuthenticated)

**Respuesta exitosa (200):**
```json
{
    "message": "Session refreshed",
    "user": {
        "username": "usuario123"
    }
}
```

**Características:**
- Verifica que la sesión siga activa
- Devuelve los datos actualizados del usuario
- Implementado como función con decoradores `@api_view`

### GET /api/auth/me/
**Descripción:** Obtiene los datos del usuario autenticado actual.

**Permisos:** Requiere autenticación (IsAuthenticated)

**Respuesta exitosa (200):**
```json
{
    "user": {
        "username": "usuario123"
    }
}
```

**Características:**
- Devuelve información del usuario de la sesión actual
- Implementado como función con decoradores `@api_view`

## Endpoints de Gestión de Usuarios

### GET /api/users/
**Descripción:** Lista todos los usuarios del sistema con paginación.

**Permisos:** Requiere autenticación (IsAuthenticated)

**Respuesta exitosa (200):**
```json
[
    {
        "username": "usuario1"
    },
    {
        "username": "usuario2"
    }
]
```

**Características:**
- Lista todos los usuarios registrados
- Implementado con `ListAPIView`
- Incluye paginación (configuración por defecto de DRF)

### GET /api/users/{id}/
**Descripción:** Obtiene los datos de un usuario específico por su ID.

**Permisos:** Requiere autenticación (IsAuthenticated)

**Parámetros de URL:**
- `id` (int): ID único del usuario

**Respuesta exitosa (200):**
```json
{
    "username": "usuario123"
}
```

**Características:**
- Implementado con `RetrieveUpdateAPIView`
- Permite tanto GET como PUT en el mismo endpoint

### PUT /api/users/{id}/
**Descripción:** Actualiza los datos de un usuario específico.

**Permisos:** Requiere autenticación (IsAuthenticated)

**Parámetros de URL:**
- `id` (int): ID único del usuario

**Cuerpo de la petición:**
```json
{
    "username": "nuevo_usuario",
    "password": "nueva_contraseña"
}
```

**Respuesta exitosa (200):**
```json
{
    "username": "nuevo_usuario"
}
```

**Características:**
- Actualización completa del usuario
- Implementado con `RetrieveUpdateAPIView`
- Valida la contraseña con las mismas reglas que el registro

## Modelos de Datos

### Usuario (User)
Modelo estándar de Django con los siguientes campos:
- `username`: Nombre de usuario único
- `password`: Contraseña hasheada
- `email`: Dirección de correo electrónico
- `first_name`: Nombre
- `last_name`: Apellido

### Tarea (Task) - Modelo definido pero endpoints no implementados
- `title`: Título de la tarea
- `description`: Descripción detallada
- `status`: Estado (todo, in_progress, done)
- `priority`: Prioridad (low, medium, high)
- `due_date`: Fecha de vencimiento
- `estimated_hours`: Horas estimadas
- `actual_hours`: Horas reales trabajadas
- `created_by`: Usuario que creó la tarea
- `assigned_ToUsers`: Usuarios asignados (relación ManyToMany)
- `tags`: Etiquetas asociadas (relación ManyToMany)
- `parent_task`: Tarea padre (relación ForeignKey a sí misma)
- `metadata`: Metadatos adicionales en formato JSON
- `created_date`: Fecha de creación
- `updated_at`: Fecha de última actualización
- `is_archived`: Indica si la tarea está archivada

### Etiqueta (Tag) - Modelo definido pero endpoints no implementados
- `name`: Nombre de la etiqueta
- `created_at`: Fecha de creación
- `updated_at`: Fecha de última actualización

## Códigos de Estado HTTP

- `200 OK`: Petición exitosa
- `201 Created`: Recurso creado exitosamente
- `400 Bad Request`: Error en la petición (datos inválidos)
- `401 Unauthorized`: No autenticado
- `403 Forbidden`: Sin permisos
- `404 Not Found`: Recurso no encontrado
- `500 Internal Server Error`: Error interno del servidor

## Configuración de Sesiones

- **Duración:** 24 horas (86400 segundos)
- **Almacenamiento:** Base de datos
- **Seguridad:** HTTPOnly habilitado
- **HTTPS:** Deshabilitado en desarrollo (cambiar en producción)

## Notas de Implementación

1. **Autenticación:** Utiliza el sistema de autenticación estándar de Django con sesiones
2. **Serializers:** Validación personalizada para contraseñas (mínimo 8 caracteres)
3. **Permisos:** La mayoría de endpoints requieren autenticación excepto registro y login
4. **Base de datos:** PostgreSQL con configuración para Docker
5. **CORS:** No configurado (necesario para aplicaciones frontend separadas)

## Endpoints Pendientes de Implementación

### Gestión de Tareas
- `GET /api/tasks/` - Listar tareas con filtros y paginación
- `POST /api/tasks/` - Crear nueva tarea
- `GET /api/tasks/{id}/` - Obtener tarea específica
- `PUT /api/tasks/{id}/` - Actualizar tarea completa
- `PATCH /api/tasks/{id}/` - Actualizar tarea parcial
- `DELETE /api/tasks/{id}/` - Eliminar tarea

### Operaciones de Tareas
- `POST /api/tasks/{id}/assign/` - Asignar tarea a usuarios
- `POST /api/tasks/{id}/comments/` - Agregar comentario
- `GET /api/tasks/{id}/comments/` - Listar comentarios
- `GET /api/tasks/{id}/history/` - Obtener historial de cambios
