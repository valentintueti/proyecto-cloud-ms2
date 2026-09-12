from typing import List
from pydantic import BaseModel
from app.models.enums import TipoServicio


class UbicacionSchema(BaseModel):
    lat: float
    lng: float


class RutaResumenSchema(BaseModel):
    ruta_id: str
    nombre: str
    tipo_servicio: TipoServicio


class ParaderoCreate(BaseModel):
    nombre: str
    ubicacion: UbicacionSchema


class ParaderoResponse(ParaderoCreate):
    id: str
    rutas: List[RutaResumenSchema] = []

    class Config:
        from_attributes = True


class ValidaConexionResponse(BaseModel):
    paradero_id: str
    ruta_id: str
    es_valida: bool 