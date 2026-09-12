from datetime import date, time
from typing import List
from pydantic import BaseModel


class ParaderoOrdenSchema(BaseModel):
    paradero_id: str
    orden: int


class ServicioCreate(BaseModel):
    ruta_id: str
    fecha: date
    hora_inicio: time
    hora_fin: time
    paraderos: List[ParaderoOrdenSchema]


class ServicioResponse(ServicioCreate):
    id: str

    class Config:
        from_attributes = True