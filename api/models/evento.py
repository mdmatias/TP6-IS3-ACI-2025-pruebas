from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Evento(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    descripcion: Optional[str] = None
    fecha_inicio: datetime
    fecha_fin: datetime
    es_cobrable: bool
    tiene_cupo: bool
    cupo_maximo: Optional[int] = None
    precio: Optional[float] = None