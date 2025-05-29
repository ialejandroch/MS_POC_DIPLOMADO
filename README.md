#MS POC DIPLOMADO

Este es un microservicio desarrollado con FastAPI para gestionar usuarios. Permite obtener la lista de usuarios, consultar un usuario por su ID y crear nuevos usuarios.

## Requisitos

- Python 3.10 o superior
- FastAPI
- Uvicorn

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>


2. Crea un entorno virtual y actívalo:
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate


Para iniciar el servidor, ejecuta el siguiente comando:

uvicorn main:app --reload


Esto iniciará el servidor en http://127.0.0.1:8000.

# Endpoints
## Obtener todos los usuarios
URL: GET /users
Descripción: Devuelve la lista de todos los usuarios.
Respuesta de ejemplo:

[
  {
    "id": 1,
    "name": "Juan Pérez",
    "email": "juan@example.com"
  },
  {
    "id": 2,
    "name": "Ana Torres",
    "email": "ana@example.com"
  }
]

## Obtener un usuario por ID
URL: GET /users/{user_id}
Descripción: Devuelve los datos de un usuario específico.
Respuesta de ejemplo:

{
  "id": 1,
  "name": "Juan Pérez",
  "email": "juan@example.com"
}

## Crear un nuevo usuario
URL: POST /users
Descripción: Crea un nuevo usuario.
Cuerpo de la solicitud:

{
  "id": 3,
  "name": "Carlos López",
  "email": "carlos@example.com"
}

Respuesta de ejemplo:
{
  "id": 3,
  "name": "Carlos López",
  "email": "carlos@example.com"
}
