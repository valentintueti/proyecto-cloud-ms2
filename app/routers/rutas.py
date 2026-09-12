from typing import Optional, List
from fastapi import APIRouter, Query
from app.schemas.ruta_schema import RutaCreate, RutaResponse
from app.services.ruta_service import ruta_service

router = APIRouter(prefix="/rutas", tags=["Rutas"])


@router.post("/", response_model=RutaResponse, status_code=201)
async def crear_ruta(ruta: RutaCreate):
    data = ruta.model_dump()
    return await ruta_service.crear_ruta(data)


@router.get("/", response_model=List[RutaResponse])
async def listar_rutas(tipo_servicio: Optional[str] = None):
    return await ruta_service.listar_rutas(tipo_servicio)


@router.get("/batch", response_model=List[RutaResponse])
async def obtener_rutas_batch(ids: str = Query(..., description="ids separados por coma, ej: R001,R002")):
    lista_ids = ids.split(",")
    return await ruta_service.obtener_rutas_batch(lista_ids)


@router.get("/{ruta_id}", response_model=RutaResponse)
async def obtener_ruta(ruta_id: str):
    return await ruta_service.obtener_ruta(ruta_id)


@router.put("/{ruta_id}", response_model=RutaResponse)
async def actualizar_ruta(ruta_id: str, cambios: RutaCreate):
    return await ruta_service.actualizar_ruta(ruta_id, cambios.model_dump())


@router.delete("/{ruta_id}", status_code=204)
async def eliminar_ruta(ruta_id: str):
    await ruta_service.eliminar_ruta(ruta_id)