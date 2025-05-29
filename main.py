from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str


users_db = [
    User(id=1, name="Juan Pérez", email="juan@example.com"),
    User(id=2, name="Ana Torres", email="ana@example.com")
]

# Obtener todos los usuarios
@app.get("/users", response_model=List[User])
def get_users():
    return users_db

# Obtener un usuario por ID
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Crear un nuevo usuario
@app.post("/users", response_model=User)
def create_user(user: User):
    users_db.append(user)
    return user
