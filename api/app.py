from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import SQLModel, Session, create_engine
from models.evento import Evento
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Configuración de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# Crear las tablas en la base de datos
SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hola Mundo!"}

@app.post("/eventos/")
def crear_evento(evento: Evento, session: Session = Depends(lambda: Session(engine))):
    try:
        session.add(evento)
        session.commit()
        session.refresh(evento)
        return {"message": "Evento creado exitosamente", "evento": evento}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))