from pydantic import BaseModel
from app.models.enums import TipoServicio, Sentido


class RutaCreate(BaseModel):
    nombre: str
    tipo_servicio: TipoServicio
    sentido: Sentido


class RutaResponse(RutaCreate):
    id: str

    class Config:
        from_attributes = True